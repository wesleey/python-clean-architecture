from abc import ABC, abstractmethod


class ICliMemoryController(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass
