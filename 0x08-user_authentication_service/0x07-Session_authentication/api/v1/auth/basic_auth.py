#!/usr/bin/env python3
"""Basic auth."""

from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """A class that inherits from Auth."""

    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """Extract."""
        basic = "Basic "
        if authorization_header is None:
            return(None)
        if not isinstance(authorization_header, str):
            return(None)
        if basic not in authorization_header:
            return(None)

        return(authorization_header.split(basic, 1)[1])

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode."""
        UTF = 'utf-8'
        if base64_authorization_header is None:
            return(None)
        if not isinstance(base64_authorization_header, str):
            return(None)
        try:
            return(b64decode(base64_authorization_header).decode(UTF))
        except Exception:
            return(None)

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Credentials."""
        colon = ":"
        if decoded_base64_authorization_header is None:
            return(None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return(None, None)
        if colon not in decoded_base64_authorization_header:
            return(None, None)
        colonSplit = decoded_base64_authorization_header.split(":", 1)[0]
        UserCred = decoded_base64_authorization_header.split(":", 1)[1]
        return(colonSplit, UserCred)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Object credentials."""
        if user_email is None:
            return(None)
        if user_pwd is None:
            return(None)
        if not isinstance(user_email, str):
            return(None)
        if not isinstance(user_pwd, str):
            return(None)
        try:
            email = User.search({'email': user_email})
        except Exception:
            return(None)
        for user in email:
            ValidUser = user.is_valid_password(user_pwd)
            if ValidUser:
                return(user)
            else:
                return(None)

    def current_user(self, request=None) -> TypeVar('User'):
        """User request."""
        AUTHORIZATION = self.authorization_header(request)
        VALUE = self.extract_base64_authorization_header(AUTHORIZATION)
        DECODE = self.decode_base64_authorization_header(VALUE)
        DECODE = self.extract_user_credentials(DECODE)
        return(self.user_object_from_credentials(DECODE[0], DECODE[1]))
