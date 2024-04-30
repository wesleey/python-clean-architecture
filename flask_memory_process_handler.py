from src.infra.db.loggers.logger_default import LoggerDefault
from src.app.flask_memory.create_flask_memory_app \
    import create_flask_memory_app


logger = LoggerDefault()


if __name__ == "__main__":
    flask_memory_app = create_flask_memory_app(logger)
    flask_memory_app.run(port=5000, debug=True)
