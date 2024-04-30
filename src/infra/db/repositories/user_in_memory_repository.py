import copy
import uuid
from typing import Dict
from src.domain.entities.user import User
from src.domain.value_objects import UserId


class UserInMemoryRepository:

    def __init__(self) -> None:
        self.__data: Dict[UserId, User] = {}

    def create(self, first_name: str, last_name: str, email: str) -> User:
        user = User(
            id=uuid.uuid4(),
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        self.__data[user.id] = copy.deepcopy(user)
        return copy.deepcopy(self.__data[user.id])

    def get(self, user_id: UserId) -> User:
        return copy.deepcopy(self.__data[user_id])
