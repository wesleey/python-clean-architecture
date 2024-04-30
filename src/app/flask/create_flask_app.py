from flask import Flask
from werkzeug.exceptions import HTTPException
from src.app.flask.blueprints.create_user_blueprint \
    import blueprint_create_user

from src.interactor.interfaces.loggers.logger_interface import ILogger
from src.interactor.errors.error_classes import UniqueViolationError


def create_flask_app(logger: ILogger):
    app = Flask(__name__)
    app.config["logger"] = logger
    app.register_blueprint(blueprint_create_user, url_prefix="/v1")

    @app.errorhandler(HTTPException)
    def handle_http_error(error: HTTPException):
        logger.log_exception(str(error.__class__.__name__))
        logger.log_exception(str(error.description))
        response = {
            "error": error.__class__.__name__,
            "message": error.description,
        }
        return response, error.code

    @app.errorhandler(ValueError)
    def handle_value_error(error: ValueError):
        return format_error_response(error, 400, logger)

    @app.errorhandler(UniqueViolationError)
    def handle_unique_violation_error(error: UniqueViolationError):
        return format_error_response(error, 409, logger)

    @app.errorhandler(Exception)
    def handle_general_exception(error: Exception):
        return format_error_response(error, 500, logger)

    return app


def format_error_response(error: Exception, error_code: int, logger: ILogger):
    logger.log_exception(f"500 - Internal Server Error: {str(error)}")
    response = {
        'status_code': error_code,
        'error': error.__class__.__name__,
        'message': str(error)
    }
    return response, error_code
