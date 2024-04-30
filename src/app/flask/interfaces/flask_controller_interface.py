from abc import ABC, abstractmethod
from typing import Dict


class IFlaskController(ABC):

    @abstractmethod
    def execute(self, input_json) -> Dict:
        pass
