import pytest
from user import *

@pytest.fixture         # does what is defined before each test
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("John Doe", "john@mail.com") == True
    assert user_manager.get_user("John Doe") == "john@mail.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("John Doe", "john@mail.com")
    with pytest.raises(ValueError):
        user_manager.add_user("John Doe", "johnDoe@mail.com")