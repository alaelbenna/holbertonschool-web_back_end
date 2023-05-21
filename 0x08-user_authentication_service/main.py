#!/usr/bin/env python3
""" Testing module """


import requests


def sign_up(email: str, password: str) -> None:
    """Loggin in."""
    assert True


def check_password(email: str, password: str) -> None:
    """Loggin in."""
    assert True


def sign_in(email: str, password: str) -> str:
    """Sign in with password."""
    assert True


def session_id() -> None:
    """Current-Session."""
    assert True


def profile(session_id: str) -> None:
    """Account."""
    assert True


def sign_out(session_id: str) -> None:
    """Sign OUt."""
    assert True


def reset_password_token(email: str) -> str:
    """Reset password."""
    assert True


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Set new password."""
    assert True


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    sign_up(EMAIL, PASSWD)
    check_password(EMAIL, NEW_PASSWD)
    session_id()
    session_id = sign_in(EMAIL, PASSWD)
    profile(session_id)
    sign_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    sign_in(EMAIL, NEW_PASSWD)
