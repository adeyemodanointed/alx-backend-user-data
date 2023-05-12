#!/usr/bin/env python3
"""Auth Module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """Hashed the password and returns a byte"""
    return bcrypt.hashpw(
            bytes(password, 'utf-8'),
            bcrypt.gensalt())


def _generate_uuid() -> str:
    """Returns a string representation os uuid"""
    uuid = uuid4()
    return str(uuid)


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

    def create_session(self, email: str) -> str:
        """Creates a user session and returns the sessionID"""
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Get a user by session_id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None
