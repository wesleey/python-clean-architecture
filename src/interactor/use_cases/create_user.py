from src.interactor.interfaces.repositories.user_repository_interface \
    import IUserRepository

from src.interactor.interfaces.presenters.create_user_presenter_interface \
    import ICreateUserPresenter

from src.interactor.interfaces.loggers.logger_interface import ILogger
from src.interactor.dtos.create_user_dto import CreateUserInputDto, CreateUserOutputDto
from src.interactor.validations.create_user_validator import CreateUserValidator
from src.interactor.errors.error_classes import NotCreatedError
from src.domain.entities.user import User
from typing import Dict


class CreateUserUseCase:

    def __init__(
        self,
        repository: IUserRepository,
        presenter: ICreateUserPresenter,
        logger: ILogger
    ) -> None:
        self.__repository = repository
        self.__presenter = presenter
        self.__logger = logger

    def execute(self, input_dto: CreateUserInputDto) -> Dict:
        validator = CreateUserValidator(input_dto.to_dict())
        validator.validate()

        user = self.__create(
            input_dto.first_name,
            input_dto.last_name,
            input_dto.email,
        )

        output_dto = CreateUserOutputDto(user)
        presenter_response = self.__presenter.present(output_dto)
        return presenter_response

    def __create(self, first_name: str, last_name: str, email: str) -> User:
        user_created = self.__repository.create(first_name, last_name, email)
        if not user_created:
            self.__logger.log_exception("User creation failed")
            raise NotCreatedError("user", f"{first_name} {last_name}".capitalize())
        self.__logger.log_info("User created successfully")
        return user_created
