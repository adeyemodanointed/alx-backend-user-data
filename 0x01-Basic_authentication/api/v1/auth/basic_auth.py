#!/usr/bin/env python3
"""Basic Auth Module"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """Returns value of decoded base64 string"""
        if (base64_authorization_header is None):
            return None
        if (type(base64_authorization_header) is not str):
            return None
        try:
            data = base64.b64decode(base64_authorization_header)
            return data.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """returns user email and password from base64 decode"""
        if (decoded_base64_authorization_header is None or
                type(decoded_base64_authorization_header) is not str):
            return None, None
        data = decoded_base64_authorization_header
        if (data.find(":") == -1):
            return None, None
        data_list = data.split(":")
        return data_list[0], data_list[1]
