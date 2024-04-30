from abc import ABC, abstractmethod
from src.domain.entities.user import User
from typing import Optional


class IUserRepository(ABC):

    @abstractmethod
    def create(self, first_name: str, last_name: str, email: int) -> Optional[User]:
        pass

    @abstractmethod
    def get(self, user_id: str) -> Optional[User]:
        pass
