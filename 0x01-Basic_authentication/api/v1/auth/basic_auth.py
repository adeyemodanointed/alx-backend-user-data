#!/usr/bin/env python3
"""Basic Auth Module"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth Class"""
    def __init__(self):
        """Initialization"""
        pass

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """Extracts base64 auth header"""
        if (authorization_header is None):
            return None
        if (type(authorization_header) is not str):
            return None
        if (authorization_header.startswith('Basic ') is False):
            return None
        else:
            return authorization_header[6:]
