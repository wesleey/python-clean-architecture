import uuid
import pytest
from typing import Dict


@pytest.fixture
def fixture_user() -> Dict[str, str]:

    return {
        "id": uuid.uuid4(),
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
    }
