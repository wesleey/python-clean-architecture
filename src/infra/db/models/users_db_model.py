# flake8: noqa

import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from src.infra.db.settings.base import Base


class UsersDBModel(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = \
        mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    first_name: Mapped[str] = \
        mapped_column(String(30), nullable=False)

    last_name: Mapped[str] = \
        mapped_column(String(30), nullable=False)

    email: Mapped[str] =  \
        mapped_column(String(200), nullable=False, unique=True)
