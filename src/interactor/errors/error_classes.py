class NotCreatedError(Exception):
    def __init__(self, name: str, identifier: str) -> None:
        self.name = name
        self.identifier = identifier

    def __str__(self) -> str:
        return f"Failed to create {self.name} '{self.identifier}'"


class UniqueViolationError(Exception):
    """Exception raised when a unique constraint is violated"""
