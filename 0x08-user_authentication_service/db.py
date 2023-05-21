#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    # Above is the default code that Holberton gave me
    # Task 1. Add User method
    def add_user(self, email: str, hashed_password: str) -> User:
        """Save the user to the Djatabase."""
        # Adding user to the Database
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Finding-the-User."""
        arguments = [
                    "id",
                    "email",
                    "hashed_password",
                    "session_id",
                    "reset_token"
                    ]
        for keyword in kwargs:
            if keyword not in arguments:
                raise(InvalidRequestError)
        userFound = self._session.query(User).filter_by(**kwargs).first()
        if userFound:
            return(userFound)
        if userFound is None:
            raise(NoResultFound)
        return(userFound)

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user to database."""
        arguments = [
                    "id",
                    "email",
                    "hashed_password",
                    "session_id",
                    "reset_token"
                    ]
        update = self.find_user_by(id=user_id)
        for keys, values in kwargs.items():
            if keys in arguments:
                setattr(update, keys, values)
            else:
                raise(ValueError)
        self._session.commit()
