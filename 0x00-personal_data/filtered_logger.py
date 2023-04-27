#!/usr/bin/env python3
"""Regex-ing"""
from typing import List
import re
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(
                    field+'=.*?'+separator,
                    field+'='+redaction+separator,
                    message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Implement the format method to filter values in incoming
        log records using filter_datum.
        Values for fields in fields should be filtered.
        """
        message = super(RedactingFormatter, self).format(record)
        new_msg = filter_datum(self.fields, self.REDACTION,
                               message, self.SEPARATOR)
        return new_msg


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
