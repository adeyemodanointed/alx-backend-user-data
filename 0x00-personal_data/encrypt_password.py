#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Password hashed function"""
    return bcrypt.hashpw(
            bytes(password, 'utf-8'),
            bcrypt.gensalt())
