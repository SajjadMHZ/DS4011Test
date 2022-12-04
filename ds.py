from typing import List, Optional


class User:
    def __init__(self, username: str, password: str):
        self.password = password
        self.username = username


class Core:
    def __init__(self):
        self._users: List[Optional[User]] = [None] * 10
        self._last_free_index = 0

    def login(self, username, password):
        for user in self._users:
            if user is None:
                break
            if user.username == username:
                if user.password == password:
                    return True
                return False  # Wrong Password
        return False  # Wrong Username

    def add_user(self, username, password):
        assert self._last_free_index < len(self._users), "Out of space for new users"
        user = User(username, password)
        self._users[self._last_free_index] = user
        self._last_free_index += 1




