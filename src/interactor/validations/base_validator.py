from typing import Dict
from cerberus import Validator


class BaseValidator:

    def __init__(self, data: Dict[str, str]) -> None:
        self.data = data
        self.errors: Dict = {}

    def verify(self, schema: Dict) -> None:
        validator = Validator(schema)
        if not validator.validate(self.data):
            self.errors = validator.errors
            self.__raise_validation_error()

    def __raise_validation_error(self):
        error_messages = []
        for field, messages in self.errors.items():
            for message in messages:
                error_messages.append(f"{field}: {message}")
        raise ValueError("\n".join(error_messages))
