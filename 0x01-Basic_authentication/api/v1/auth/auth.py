#!/usr/bin/env python3
"""Auth class"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """Auth Class"""
    def __init__(self):
        """Initialization"""
        pass

    def require_auth(
            self,
            path: str,
            excluded_paths: List[str]) -> bool:
        """Check paths that require auth"""
        if (path is None or
                excluded_paths is None or
                excluded_paths == []):
            return True
        if (path in excluded_paths
                or path+"/" in excluded_paths):
            return False
        for a_path in excluded_paths:
            if re.search(a_path.replace("*", "+"), path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header method"""
        if (request is None):
            return None
        if (request.headers.get('authorization') is None):
            return None
        return request.headers['authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Checks for current user"""
        self.request = request
        return None
