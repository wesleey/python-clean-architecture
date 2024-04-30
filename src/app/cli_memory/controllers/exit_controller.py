import sys
from src.app.cli_memory.interfaces.cli_memory_controller_interface \
    import ICliMemoryController


class ExitController(ICliMemoryController):

    def execute(self) -> None:
        print("Exiting the program.")
        sys.exit()
