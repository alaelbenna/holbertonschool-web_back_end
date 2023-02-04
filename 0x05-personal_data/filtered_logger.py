#!/usr/bin/env python3
"""RedactingFormatter module"""

import logging
import mysql.connector
import os
import re
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records using filter_datum method"""
        original = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION, original,
                            self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    filter_datum: a function that returns the log message obfuscated

    Args:
        fields (list): a list of strings representing all fields to obfuscate
        redaction (str): a string representing by what the field
        will be obfuscated
        message (str): a string representing the log line
        separator (str): a string representing by which character
        is separating all fields in the log line

    returns: a string
    """
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formater = RedactingFormatter(PII_FIELDS)
    ch.setFormatter(formater)

    logger.addHandler(ch)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""

    user = os.getenv("PERSONAL_DATA_DB_USERNAME", 'root')
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", '')
    host = os.getenv("PERSONAL_DATA_DB_HOST", 'localhost')
    db = os.getenv("PERSONAL_DATA_DB_NAME")

    conn = mysql.connector.connect(
        host=host,
        database=db,
        user=user,
        password=password
    )

    return conn


def main() -> None:
    """
    connect to a database with get_db, retrieve all rows
    from users table and display filtered rows
    """
    db = get_db()
    user = "SELECT * FROM users"
    filtered-fields = [i[0] for i in cursor.description]
    log = get_logger()
    with db.cursor() as cursor:
        cursor.execute(user)

        for row in cursor.fetchall():
            record = ""
            for j in range(len(filtered-fields)):
                record += filtered-fields[j] + '=' + str(row[j]) + ';'
            log.info(record)


if __name__ == '__main__':
    main()
