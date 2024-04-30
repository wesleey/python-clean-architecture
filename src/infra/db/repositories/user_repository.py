import uuid
from sqlalchemy.exc import IntegrityError
from src.interactor.errors.error_classes import UniqueViolationError
from src.interactor.interfaces.repositories.user_repository_interface \
    import IUserRepository

from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.models.users_db_model \
    import UsersDBModel as UserEntity

from src.domain.entities.user import User
from src.domain.value_objects import UserId
from typing import Optional


class UserRepository(IUserRepository):

    def create(cls, first_name: str, last_name: str, email: str) -> Optional[User]:
        with DBConnectionHandler() as database:
            try:
                new_registry = UserEntity(
                    id=uuid.uuid4(),
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
                database.session.add(new_registry)
                database.session.commit()
                return User(
                    id=new_registry.id,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
            except IntegrityError as exception:
                if "violates unique constraint" in str(exception.orig):
                    raise UniqueViolationError(
                        "User with the same email already exists"
                    ) from exception
                raise
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get(cls, user_id: UserId) -> Optional[User]:
        with DBConnectionHandler() as database:
            try:
                user = database.session.get(UserEntity, user_id)
                if user is not None:
                    return User(
                        id=user.id,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        email=user.email,
                    )
                return None
            except Exception as exception:
                database.session.rollback()
                raise exception
