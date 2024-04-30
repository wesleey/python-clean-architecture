from typing import Dict
from src.app.flask.interfaces.flask_controller_interface import IFlaskController
from src.infra.db.repositories.user_repository import UserRepository
from src.app.flask.presenters.create_user_presenter import CreateUserPresenter
from src.interactor.interfaces.loggers.logger_interface import ILogger
from src.interactor.use_cases.create_user import CreateUserUseCase
from src.interactor.dtos.create_user_dto import CreateUserInputDto


class CreateUserController(IFlaskController):

    def __init__(self, logger: ILogger) -> None:
        self.__logger = logger

    def execute(self, json_input) -> Dict:
        repository = UserRepository()
        presenter = CreateUserPresenter()
        logger = self.__logger
        use_case = CreateUserUseCase(repository, presenter, logger)
        input_dto = self.get_user_info(json_input)
        return use_case.execute(input_dto)

    def get_user_info(self, json) -> CreateUserInputDto:
        if "first_name" in json:
            first_name = json["first_name"]
        else:
            raise ValueError("Missing first name")

        if "last_name" in json:
            last_name = json["last_name"]
        else:
            raise ValueError("Missing last name")

        if "email" in json:
            email = json["email"]
        else:
            raise ValueError("Missing email")

        return CreateUserInputDto(first_name, last_name, email)
