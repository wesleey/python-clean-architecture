import pytest
from .create_user_validator import CreateUserValidator
from .base_schema import first_name_schema, last_name_schema, email_schema


def test_create_user_validator_with_valid_data(mocker, fixture_user):
    mocker.patch("src.interactor.validations.base_validator.BaseValidator.verify")

    input_data = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": fixture_user["email"],
    }

    validator = CreateUserValidator(input_data)
    validator.validate()

    schema = {
        "first_name": first_name_schema,
        "last_name": last_name_schema,
        "email": email_schema,
    }

    validator.verify.assert_called_once_with(schema)


def test_create_user_validator_with_empty_value(fixture_user):
    input_data = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": "",
    }

    validator = CreateUserValidator(input_data)

    with pytest.raises(ValueError) as exception_info:
        validator.validate()

    assert str(exception_info.value) == "email: empty values not allowed"
