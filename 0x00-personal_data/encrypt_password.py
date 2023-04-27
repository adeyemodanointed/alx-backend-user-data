#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Password hashed function"""
    return bcrypt.hashpw(
            bytes(password, 'utf-8'),
            bcrypt.gensalt())


def is_valid(
        hashed_password: bytes,
        password: str) -> bool:
    """Check if password is valid"""
    return bcrypt.checkpw(
            bytes(password, 'utf-8'),
            hashed_password)
