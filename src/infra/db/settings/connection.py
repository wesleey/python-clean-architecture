from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from configs import config as config_app


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__engine: Engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self) -> Engine:
        engine = create_engine(config_app.DB_URI)
        return engine

    def get_engine(self) -> Engine:
        return self.__engine

    def __enter__(self):
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
