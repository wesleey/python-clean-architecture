from src.interactor.interfaces.presenters.create_user_presenter_interface \
    import ICreateUserPresenter

from src.interactor.dtos.create_user_dto import CreateUserOutputDto
from typing import Dict


class CreateUserPresenter(ICreateUserPresenter):

    def present(self, output_dto: CreateUserOutputDto) -> Dict:
        return {
            "id": output_dto.user.id,
            "first_name": output_dto.user.first_name,
            "last_name": output_dto.user.last_name,
            "email": output_dto.user.email,
        }
