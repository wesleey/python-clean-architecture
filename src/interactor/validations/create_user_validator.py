from typing import Dict
from .base_validator import BaseValidator
from .base_schema import first_name_schema, last_name_schema, email_schema


class CreateUserValidator(BaseValidator):

    def __init__(self, input_data: Dict) -> None:
        super().__init__(input_data)

        self.__schema = {
            "first_name": first_name_schema,
            "last_name": last_name_schema,
            "email": email_schema,
        }

    def validate(self) -> None:
        super().verify(self.__schema)
