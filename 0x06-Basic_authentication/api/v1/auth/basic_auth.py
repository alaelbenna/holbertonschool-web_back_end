#!/usr/bin/env python3
"""basic auth module"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic ") \
                and not authorization_header.endswith(" "):
            return None

        return "".join(list(authorization_header)[6:])

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        returns the decoded value of a
        Base64 string base64_authorization_header
        """

        if base64_authorization_header is None \
                or not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(base64_authorization_header) \
                    .decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from the Base64 decoded value"""

        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if decoded_base64_authorization_header.find(':') == -1:
            return None, None

        return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):

        """returns the User instance based on his email and password"""

        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        obj = User().search({"email": user_email})
        if not obj:
            return None
        if obj[0].is_valid_password(user_pwd):
            return obj[0]
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request"""

        head = self.authorization_header(request)
        base64 = self.extract_base64_authorization_header(head)
        decoded = self.decode_base64_authorization_header(base64)
        cred = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(cred[0], cred[1])