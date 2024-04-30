from .user_in_memory_repository import UserInMemoryRepository


def test_user_in_memory_repository(fixture_user):
    repository = UserInMemoryRepository()

    user_created = repository.create(
        first_name=fixture_user["first_name"],
        last_name=fixture_user["last_name"],
        email=fixture_user["email"],
    )

    assert user_created.first_name == fixture_user["first_name"]
    assert user_created.last_name == fixture_user["last_name"]
    assert user_created.email == fixture_user["email"]

    user = repository.get(user_created.id)

    assert user.id == user_created.id
    assert user.first_name == user_created.first_name
    assert user.last_name == user_created.last_name
    assert user.email == user_created.email
