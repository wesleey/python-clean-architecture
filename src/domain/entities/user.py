from dataclasses import dataclass, asdict
from src.domain.value_objects import UserId
from typing import Dict


@dataclass
class User:
    id: UserId
    first_name: str
    last_name: str
    email: str

    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        return cls(**data)

    def to_dict(self) -> Dict:
        return asdict(self)
