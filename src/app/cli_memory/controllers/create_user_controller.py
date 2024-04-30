from src.app.cli_memory.interfaces.cli_memory_controller_interface \
    import ICliMemoryController

from src.infra.db.repositories.user_in_memory_repository \
    import UserInMemoryRepository

from src.app.cli_memory.presenters.create_user_presenter \
    import CreateUserPresenter

from src.interactor.interfaces.loggers.logger_interface import ILogger
from src.interactor.use_cases.create_user import CreateUserUseCase
from src.app.cli_memory.views.create_user_view import CreateUserView
from src.interactor.dtos.create_user_dto import CreateUserInputDto


class CreateUserController(ICliMemoryController):

    def __init__(self, logger: ILogger) -> None:
        self.__logger = logger

    def execute(self) -> None:
        repository = UserInMemoryRepository()
        presenter = CreateUserPresenter()
        logger = self.__logger
        use_case = CreateUserUseCase(repository, presenter, logger)
        input_dto = self.__get_user_info()
        result = use_case.execute(input_dto)
        view = CreateUserView()
        view.show(result)

    def __get_user_info(self) -> CreateUserInputDto:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        return CreateUserInputDto(first_name, last_name, email)
