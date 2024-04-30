import pytest
from .create_user_controller import CreateUserController
from src.interactor.interfaces.loggers.logger_interface import ILogger
from src.interactor.dtos.create_user_dto import CreateUserInputDto


@pytest.fixture
def logger_mock(mocker):
    return mocker.patch.object(ILogger, "log_info")


def test_create_user_controller(mocker, logger_mock, monkeypatch, fixture_user):
    repository_mock = mocker.patch("src.app.flask_memory.controllers.\
create_user_controller.UserInMemoryRepository")
    presenter_mock = mocker.patch("src.app.flask_memory.controllers.\
create_user_controller.CreateUserPresenter")
    use_case_mock = mocker.patch("src.app.flask_memory.controllers.\
create_user_controller.CreateUserUseCase")

    use_case_result = {
        "id": fixture_user["id"],
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": fixture_user["email"],
    }

    use_case_instance = use_case_mock.return_value
    use_case_instance.execute.return_value = use_case_result

    fake_user_inputs = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": fixture_user["email"],
    }

    monkeypatch.setattr('builtins.input', lambda _: next(fake_user_inputs))

    controller = CreateUserController(logger_mock)
    result = controller.execute(fake_user_inputs)

    repository_mock.assert_called_once_with()
    presenter_mock.assert_called_once_with()
    use_case_mock.assert_called_once_with(
        repository_mock.return_value,
        presenter_mock.return_value,
        logger_mock
    )

    input_dto = CreateUserInputDto(
        first_name=fixture_user["first_name"],
        last_name=fixture_user["last_name"],
        email=fixture_user["email"],
    )

    use_case_instance.execute.assert_called_once_with(input_dto)

    assert result["first_name"] == fixture_user["first_name"]
    assert result["last_name"] == fixture_user["last_name"]
    assert result["email"] == fixture_user["email"]


def test_missing_inputs(logger_mock, fixture_user):
    controller = CreateUserController(logger_mock)

    # Missing first name
    fake_user_inputs = {
        "last_name": fixture_user["first_name"],
        "email": fixture_user["email"],
    }

    with pytest.raises(ValueError) as exception_info:
        controller.get_user_info(fake_user_inputs)

    assert str(exception_info.value) == "Missing first name"

    # Missing last name
    fake_user_inputs = {
        "first_name": fixture_user["first_name"],
        "email": fixture_user["email"],
    }

    with pytest.raises(ValueError) as exception_info:
        controller.get_user_info(fake_user_inputs)

    assert str(exception_info.value) == "Missing last name"

    # Missing email
    fake_user_inputs = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
    }

    with pytest.raises(ValueError) as exception_info:
        controller.get_user_info(fake_user_inputs)

    assert str(exception_info.value) == "Missing email"
