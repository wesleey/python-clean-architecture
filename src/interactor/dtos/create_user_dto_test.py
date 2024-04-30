from .create_user_dto import CreateUserInputDto


def test_create_user_input_dto(fixture_user):
    input_dto = CreateUserInputDto(
        first_name=fixture_user["first_name"],
        last_name=fixture_user["last_name"],
        email=fixture_user["email"],
    )

    assert input_dto.first_name == fixture_user["first_name"]
    assert input_dto.last_name == fixture_user["last_name"]
    assert input_dto.email == fixture_user["email"]

    user_dict = {
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": fixture_user["email"],
    }

    assert input_dto.to_dict() == user_dict
