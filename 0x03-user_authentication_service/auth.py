#!/usr/bin/env python3
"""Auth Module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashed the password and returns a byte"""
    return bcrypt.hashpw(
            bytes(password, 'utf-8'),
            bcrypt.gensalt())
