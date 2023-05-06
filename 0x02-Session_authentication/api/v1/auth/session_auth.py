#!/usr/bin/env python3
"""Session Auth module"""
from api.v1.auth.auth import Auth
import uuid


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
        self.user_id_by_session_id[new_key] = user_id
        return new_key
