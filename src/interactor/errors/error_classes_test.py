import pytest
from .error_classes import NotCreatedError


def test_not_created_error():
    with pytest.raises(NotCreatedError) as exception:
        raise NotCreatedError("user", "John Doe")

    assert str(exception.value) == "Failed to create user 'John Doe'"
