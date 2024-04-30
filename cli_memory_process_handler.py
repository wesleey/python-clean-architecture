from typing import Dict
from src.infra.db.loggers.logger_default import LoggerDefault
from src.interactor.interfaces.loggers.logger_interface import ILogger
from src.app.cli_memory.controllers.exit_controller import ExitController

from src.app.cli_memory.interfaces.cli_memory_controller_interface \
    import ICliMemoryController

from src.app.cli_memory.controllers.create_user_controller \
    import CreateUserController


class CliMemoryProcessHandler:

    def __init__(self, logger: ILogger) -> None:
        self.__logger = logger
        self.__options: Dict = {}

    def execute(self) -> None:
        print("Please choose an option: ")
        self.show_options()
        choice = input("Choice: ")
        option = self.__options.get(choice)
        if option:
            try:
                option.execute()
            except ValueError as exception_info:
                print("Error: " + str(exception_info))
                self.__logger.log_exception(str(exception_info))
        else:
            print("Invalid choice.")
            self.__logger.log_info("Invalid user choice: " + option)

    def add_option(self, option: str, controller: ICliMemoryController) -> None:
        self.__options[option] = controller

    def show_options(self):
        for option, controller in self.__options.items():
            print(option + ": " + controller.__class__.__name__)


if __name__ == "__main__":
    logger_default = LoggerDefault()
    process = CliMemoryProcessHandler(logger_default)
    process.add_option("0", ExitController())
    process.add_option("1", CreateUserController(logger_default))
    process.execute()
