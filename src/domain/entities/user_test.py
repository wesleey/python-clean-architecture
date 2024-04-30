from .user import User


def test_user_creation(fixture_user):
    user = User(
        id=fixture_user["id"],
        first_name=fixture_user["first_name"],
        last_name=fixture_user["last_name"],
        email=fixture_user["email"],
    )

    assert user.id == fixture_user["id"]
    assert user.first_name == fixture_user["first_name"]
    assert user.last_name == fixture_user["last_name"]
    assert user.email == fixture_user["email"]


def test_user_from_dict(fixture_user):
    user = User.from_dict(fixture_user)

    assert user.id == fixture_user["id"]
    assert user.first_name == fixture_user["first_name"]
    assert user.last_name == fixture_user["last_name"]
    assert user.email == fixture_user["email"]


def test_user_to_dict(fixture_user):
    user = User.from_dict(fixture_user)
    assert user.to_dict() == fixture_user


def test_user_comparison(fixture_user):
    user_1 = User.from_dict(fixture_user)
    user_2 = User.from_dict(fixture_user)
    assert user_1 == user_2
