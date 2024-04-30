from .create_user_controller import CreateUserController
from src.interactor.interfaces.loggers.logger_interface import ILogger
from src.interactor.dtos.create_user_dto import CreateUserInputDto


def test_create_user_controller(mocker, monkeypatch, fixture_user):
    repository_mock = mocker.patch("src.app.cli_memory.controllers.\
create_user_controller.UserInMemoryRepository")
    presenter_mock = mocker.patch("src.app.cli_memory.controllers.\
create_user_controller.CreateUserPresenter")
    logger_mock = mocker.patch.object(ILogger, "log_info")
    use_case_mock = mocker.patch("src.app.cli_memory.controllers.\
create_user_controller.CreateUserUseCase")
    view_mock = mocker.patch("src.app.cli_memory.controllers.\
create_user_controller.CreateUserView")

    use_case_result = {
        "id": fixture_user["id"],
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": fixture_user["email"],
    }

    use_case_instance = use_case_mock.return_value
    use_case_instance.execute.return_value = use_case_result

    view_instance = view_mock.return_value

    fake_user_inputs = iter([
        fixture_user["first_name"],
        fixture_user["last_name"],
        fixture_user["email"],
    ])

    monkeypatch.setattr('builtins.input', lambda _: next(fake_user_inputs))

    controller = CreateUserController(logger_mock)
    controller.execute()

    repository_mock.assert_called_once_with()
    presenter_mock.assert_called_once_with()
    use_case_mock.assert_called_once_with(
        repository_mock.return_value,
        presenter_mock.return_value,
        logger_mock,
    )

    input_dto = CreateUserInputDto(
        first_name=fixture_user["first_name"],
        last_name=fixture_user["last_name"],
        email=fixture_user["email"],
    )

    use_case_instance.execute.assert_called_once_with(input_dto)
    view_instance.show.assert_called_once_with(use_case_result)
