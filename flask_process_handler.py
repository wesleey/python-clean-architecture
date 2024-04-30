from src.infra.db.loggers.logger_default import LoggerDefault
from src.app.flask.create_flask_app import create_flask_app


logger = LoggerDefault()


if __name__ == "__main__":
    flask_app = create_flask_app(logger)
    flask_app.run(port=5000, debug=True)
