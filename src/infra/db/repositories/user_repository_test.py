import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .user_repository import UserRepository


@pytest.fixture
def connection():
    db_connection_handler = DBConnectionHandler()
    connection = db_connection_handler.get_engine().connect()
    return connection


@pytest.mark.skip(reason="Test requires database connection")
def test_create_user(fixture_user, connection):
    user_repository = UserRepository()

    user_repository.create(
        fixture_user["first_name"],
        fixture_user["last_name"],
        fixture_user["email"],
    )

    sql = f'''
        SELECT * FROM users
        WHERE first_name = '{fixture_user["first_name"]}'
        AND last_name = '{fixture_user["last_name"]}'
        AND email = '{fixture_user["email"]}'
    '''

    response = connection.execute(text(sql))
    registry = response.fetchone()

    assert registry.first_name == fixture_user["first_name"]
    assert registry.last_name == fixture_user["last_name"]
    assert registry.email == fixture_user["email"]

    connection.execute(text(f'''
        DELETE FROM users
        WHERE id = '{registry.id}'
    '''))
    connection.commit()


@pytest.mark.skip(reason="Test requires database connection")
def test_find_user(fixture_user, connection):
    sql = '''
        INSERT INTO users (id, first_name, last_name, email)
        VALUES ('{}', '{}', '{}', '{}')
    '''.format(
        fixture_user["id"],
        fixture_user["first_name"],
        fixture_user["last_name"],
        fixture_user["email"]
    )

    connection.execute(text(sql))
    connection.commit()

    user_repository = UserRepository()
    user = user_repository.get(fixture_user["id"])

    assert user.first_name == fixture_user["first_name"]
    assert user.last_name == fixture_user["last_name"]
    assert user.email == fixture_user["email"]

    connection.execute(text(f'''
        DELETE FROM users
        WHERE id = '{user.id}'
    '''))
    connection.commit()
