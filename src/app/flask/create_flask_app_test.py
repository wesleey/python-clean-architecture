import pytest
from unittest import mock
from .create_flask_app import create_flask_app
from src.infra.db.loggers.logger_default import LoggerDefault

with mock.patch("sqlalchemy.create_engine") as create_engine_mock:
    from src.app.flask.controllers.create_user_controller \
        import CreateUserController


logger = LoggerDefault()


@pytest.fixture
def app_flask_app():
    app = create_flask_app(logger)
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture
def client_flask_app(app_flask_app):
    return app_flask_app.test_client()


@pytest.mark.skip(reason="Test requires database connection")
def test_request_user(client_flask_app, fixture_user):
    input_data = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": fixture_user["email"],
    }

    response = client_flask_app.post("/v1/user/", json=input_data)

    assert fixture_user["first_name"].encode() in response.data
    assert fixture_user["last_name"].encode() in response.data
    assert fixture_user["email"].encode() in response.data


@pytest.mark.skip(reason="Test requires database connection")
def test_request_user_missing_email_error(client_flask_app, fixture_user):
    input_data = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
    }

    response = client_flask_app.post("/v1/user/", json=input_data)
    assert b"Missing email" in response.data


@pytest.mark.skip(reason="Test requires database connection")
def test_request_user_wrong_url_error(client_flask_app, fixture_user):
    input_data = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": fixture_user["email"],
    }

    response = client_flask_app.post("/v1/usr/", json=input_data)
    assert b"The requested URL was not found on the server" in response.data


@pytest.mark.skip(reason="Test requires database connection")
def test_request_user_500_status_code(client_flask_app, mocker, fixture_user):
    blueprint_mock = mocker.patch.object(CreateUserController, "get_user_info")
    blueprint_mock.side_effect = Exception('Unexpected error!')

    input_data = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": fixture_user["email"],
    }

    response = client_flask_app.post("/v1/user/", json=input_data)
    assert b'"status_code":500' in response.data
