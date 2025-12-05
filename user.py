from typing import List, Tuple, Optional

class UserManager:
    def __init__(self) -> None:
        self._users: List[Tuple[str, str]] = []

    def add_user(self, name: str, email: str) -> bool:
        for existing_name, _ in self._users:
            if existing_name == name:
                raise ValueError(f"User with name '{name}' already exists")

        self._users.append((name, email))
        return True

    def get_user(self, name: str) -> Optional[str]:
        for existing_name, email in self._users:
            if existing_name == name:
                return email
        return None