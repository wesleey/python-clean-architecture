import pytest
from .create_flask_memory_app import create_flask_memory_app
from src.infra.db.loggers.logger_default import LoggerDefault
from src.app.flask_memory.controllers.create_user_controller \
    import CreateUserController


logger = LoggerDefault()


@pytest.fixture
def app_flask_memory_app():
    app = create_flask_memory_app(logger)
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture
def client_flask_memory_app(app_flask_memory_app):
    return app_flask_memory_app.test_client()


def test_request_user(client_flask_memory_app, fixture_user):
    input_data = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": fixture_user["email"],
    }

    response = client_flask_memory_app.post("/v1/user/", json=input_data)

    assert fixture_user["first_name"].encode() in response.data
    assert fixture_user["last_name"].encode() in response.data
    assert fixture_user["email"].encode() in response.data


def test_request_user_missing_email_error(client_flask_memory_app, fixture_user):
    input_data = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
    }

    response = client_flask_memory_app.post("/v1/user/", json=input_data)
    assert b"Missing email" in response.data


def test_request_user_wrong_url_error(client_flask_memory_app, fixture_user):
    input_data = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": fixture_user["email"],
    }

    response = client_flask_memory_app.post("/v1/usr/", json=input_data)
    assert b"The requested URL was not found on the server" in response.data


def test_request_user_500_status_code(client_flask_memory_app, mocker, fixture_user):
    blueprint_mock = mocker.patch.object(CreateUserController, "get_user_info")
    blueprint_mock.side_effect = Exception('Unexpected error!')

    input_data = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": fixture_user["email"],
    }

    response = client_flask_memory_app.post("/v1/user/", json=input_data)
    assert b'"status_code":500' in response.data
