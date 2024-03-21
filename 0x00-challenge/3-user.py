#!/usr/bin/python3
"""
Module for User class.
Defines a User class with a private password attribute and methods to
validate the password.
"""

import hashlib
import uuid


class User:
    """User class for a system with password management."""
    __password = None

    def __init__(self):
        """Initialize a new user with a unique id."""
        self.id = str(uuid.uuid4())

    @property
    def password(self):
        """Password property getter."""
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Password setter that hashes the password with MD5.
        Args:
            pwd (str): The password to hash.
        """
        if pwd is None or not isinstance(pwd, str):
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest()

    def is_valid_password(self, pwd):
        """
        Check if a password is valid.
        Args:
            pwd (str): The password to validate.
        Returns:
            bool: True if the password is valid, False otherwise.
        """
        if pwd is None or not isinstance(pwd, str):
            return False
        if self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest() == self.__password


if __name__ == '__main__':
    print("Test User")

    user = User()
    user.password = "my_secret_password"
    print(user.is_valid_password("my_secret_password"))
    print(user.is_valid_password("wrong_password"))
