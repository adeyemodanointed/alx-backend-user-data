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
    for field in fields:
        message = re.sub(
                    r'{}=[a-zA-Z0-9/@]+{}'.format(field, separator),
                    '{}={}{}'.format(field, redaction, separator),
                    message)
    return message
