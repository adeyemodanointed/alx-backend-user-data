#!/usr/bin/env python3
"""Session Auth module"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """SessionAuth Class"""

    user_id_by_session_id = {}

    def __init__(self):
        """Initialization"""
        pass

    def create_session(self, user_id: str = None) -> str:
        """Creates a session"""
        if user_id is None or type(user_id) is not str:
            return None

        new_key = uuid.uuid4()
        self.user_id_by_session_id[str(new_key)] = user_id
        return str(new_key)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns userId based on sessionId"""
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Overload function for current user"""
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        return User.get(user_id)
