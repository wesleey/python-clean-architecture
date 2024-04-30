from .create_user_presenter import CreateUserPresenter
from src.interactor.dtos.create_user_dto import CreateUserOutputDto
from src.domain.entities.user import User


def test_create_user_presenter(fixture_user):
    presenter = CreateUserPresenter()

    user = User(
        id=fixture_user["id"],
        first_name=fixture_user["first_name"],
        last_name=fixture_user["last_name"],
        email=fixture_user["email"],
    )

    output_dto = CreateUserOutputDto(user)

    expected_response = {
        "id": fixture_user["id"],
        "first_name": fixture_user["first_name"],
        "last_name": fixture_user["last_name"],
        "email": fixture_user["email"],
    }

    assert presenter.present(output_dto) == expected_response
