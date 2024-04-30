import pytest
from unittest.mock import patch
from .create_user import CreateUserUseCase

from src.interactor.interfaces.repositories.user_repository_interface \
    import IUserRepository

from src.interactor.interfaces.presenters.create_user_presenter_interface \
    import ICreateUserPresenter

from src.interactor.interfaces.loggers.logger_interface import ILogger
from src.interactor.dtos.create_user_dto import CreateUserInputDto, CreateUserOutputDto
from src.interactor.errors.error_classes import NotCreatedError
from src.domain.entities.user import User


@pytest.fixture
def repository(mocker, fixture_user):
    repository = mocker.patch.object(IUserRepository, "create")
    repository.create.return_value = User(
        id=fixture_user["id"],
        first_name=fixture_user["first_name"],
        last_name=fixture_user["last_name"],
        email=fixture_user["email"],
    )
    return repository


@pytest.fixture
def presenter(mocker):
    return mocker.patch.object(ICreateUserPresenter, "present")


@pytest.fixture
def logger(mocker):
    return mocker.patch.object(ILogger, "log_info")


@patch("src.interactor.use_cases.create_user.CreateUserValidator")
def test_create_user(validator, repository, presenter, logger, fixture_user):
    presenter.present.return_value = "Test output"

    input_dto = CreateUserInputDto(
        first_name=fixture_user["first_name"],
        last_name=fixture_user["last_name"],
        email=fixture_user["email"]
    )

    use_case = CreateUserUseCase(repository, presenter, logger)

    assert use_case.execute(input_dto) == presenter.present.return_value

    validator.assert_called_once_with(input_dto.to_dict())
    validator_instance = validator.return_value
    validator_instance.validate.assert_called_once()

    repository.create.assert_called_once_with(
        fixture_user["first_name"],
        fixture_user["last_name"],
        fixture_user["email"]
    )

    logger.log_info.assert_called_once_with("User created successfully")

    output_dto = CreateUserOutputDto(repository.create.return_value)
    presenter.present.assert_called_once_with(output_dto)

    # Testing None return value from repository
    repository.create.return_value = None

    with pytest.raises(NotCreatedError) as exception:
        use_case.execute(input_dto)

    name = f"{fixture_user['first_name']} {fixture_user['last_name']}"

    assert str(exception.value) == f"Failed to create user '{name.capitalize()}'"


def test_create_user_with_empty_value(repository, presenter, logger, fixture_user):
    use_case = CreateUserUseCase(presenter, repository, logger)

    input_dto = CreateUserInputDto(
        first_name=fixture_user["first_name"],
        last_name=fixture_user["last_name"],
        email=""
    )

    with pytest.raises(ValueError) as exception_info:
        use_case.execute(input_dto)

    assert str(exception_info.value) == "email: empty values not allowed"

    presenter.assert_not_called()
    repository.assert_not_called()
