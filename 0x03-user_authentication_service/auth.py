#!/usr/bin/env python3
"""Auth Module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hashed the password and returns a byte"""
    return bcrypt.hashpw(
            bytes(password, 'utf-8'),
            bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user with email and password"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(
                        'User {} already exists'.format(email))
        except NoResultFound:
            hashp = _hash_password(password)
            return self._db.add_user(email, hashp)

    def valid_login(self, email: str, password: str) -> bool:
        """Checks for a valid login"""
        try:
            user = self._db.find_user_by(email=email)
            if user is None:
                return False
            else:
                return bcrypt.checkpw(
                        bytes(password, 'utf-8'),
                        user.hashed_password)
            return False
        except Exception:
            return False
