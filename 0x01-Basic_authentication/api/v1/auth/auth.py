#!/usr/bin/env python3
"""Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth Class"""
    def __init__(self):
        pass

    def require_auth(
            self,
            path: str,
            excluded_paths: List[str]) -> bool:
        """Check paths that require auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header method"""
        self.request = request
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Checks for current user"""
        self.request = request
        return None
