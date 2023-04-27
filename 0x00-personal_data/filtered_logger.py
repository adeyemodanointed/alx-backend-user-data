#!/usr/bin/env python3
"""Regex-ing"""
from typing import List
import re


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str):
    """returns the log message obfuscated"""
    new_msg = message
    for field in fields:
        new_msg = re.sub(
                    r'{}=[a-zA-Z0-9/@]+{}'.format(field, separator),
                    '{}={}{}'.format(field, redaction, separator),
                    new_msg)
    return new_msg
