import pytest
from .base_validator import BaseValidator
from typing import Dict


class Validator(BaseValidator):
    def __init__(self, data: Dict):
        super().__init__(data)
        self.schema = {
            "name": {
                "type": "string",
                "minlength": 3,
                "maxlength": 10,
                "required": True,
                "empty": False,
            },
        }

    def validate(self):
        super().verify(self.schema)


def test_base_validator_with_valid_data():
    data = {"name": "test"}
    validator = Validator(data)
    validator.validate()


def test_base_validator_with_small_data():
    data = {"name": "a"}
    validator = Validator(data)
    with pytest.raises(ValueError) as exception_info:
        validator.validate()
    assert str(exception_info.value) == "name: min length is 3"


def test_base_validator_with_long_data():
    data = {"name": "This is a long name"}
    validator = Validator(data)
    with pytest.raises(ValueError) as exception_info:
        validator.validate()
    assert str(exception_info.value) == "name: max length is 10"


def test_base_validator_with_empty_value():
    data = {"name": ""}
    validator = Validator(data)
    with pytest.raises(ValueError) as exception_info:
        validator.validate()
    assert str(exception_info.value) == "name: empty values not allowed"


def test_base_validator_without_required_field():
    data = {}
    validator = Validator(data)
    with pytest.raises(ValueError) as exception_info:
        validator.validate()
    assert str(exception_info.value) == "name: required field"
