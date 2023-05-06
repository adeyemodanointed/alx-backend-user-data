#!/usr/bin/env python3
"""Basic Auth Module"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


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
        return data_list[0], ":".join(data_list[1:])

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if (user_email is None or user_pwd is None or
                type(user_email) is not str or
                type(user_pwd) is not str):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get current user for a request"""
        auth_header = self.authorization_header(request)
        ext_header = self.extract_base64_authorization_header(
            auth_header)
        decoded_hdr = self.decode_base64_authorization_header(
            ext_header)
        credential = self.extract_user_credentials(decoded_hdr)
        return self.user_object_from_credentials(credential[0], credential[1])
