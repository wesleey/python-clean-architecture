from abc import ABC, abstractmethod
from src.interactor.dtos.create_user_dto import CreateUserOutputDto
from typing import Dict


class ICreateUserPresenter(ABC):

    @abstractmethod
    def present(self, output_dto: CreateUserOutputDto) -> Dict:
        pass
