#!/usr/bin/env python3
"""Basic Bebel Setup."""


from flask import Flask, request
from flask import render_template
from flask_babel import Babel
import flask
import typing
import os

# outside the scope of this project
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Babel Flask Configuration."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object('5-app.Config')
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def Basic_Flask():
    """Basic-Flask-App."""
    return(render_template('5-index.html'))


@babel.localeselector
def get_locale():
    """Locale from request."""
    URLparameter = request.args.get('locale')
    Languages = app.config['LANGUAGES']
    if URLparameter:
        if URLparameter in Languages:
            return(URLparameter)
    elif flask.g.user('locale')\
            and flask.g.user.get('locale') in app.config['LANGUAGES']:
        return(flask.g.user.get('locale'))
    else:
        return(request.accept_languages.best_match(app.config['LANGUAGES']))


def get_user() -> typing.Union[dict, None]:
    """Mock loggin in."""
    login = request.args.get('login_as')
    password = int(request.args.get('login_as'))
    if login:
        if password in users:
            return(users.get(password))
    else:
        return(None)


@app.before_request
def before_request():
    """Before all functions - Decorator to make it be executed."""
    flask.g.user = get_user()


if __name__ == "__main__":
    IPaddress = os.getenv("API_HOST", "0.0.0.0")
    app.run(host=IPaddress, port='5000')
