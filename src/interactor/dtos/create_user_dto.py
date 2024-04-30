from dataclasses import dataclass, asdict
from src.domain.entities.user import User
from typing import Dict


@dataclass
class CreateUserInputDto:
    first_name: str
    last_name: str
    email: str

    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class CreateUserOutputDto:
    user: User

    def to_dict(self) -> Dict:
        return asdict(self)
