#!/usr/bin/env python3
"""Basic Bebel Setup."""


from flask import Flask, request
from flask import render_template
from flask_babel import Babel
import os


class Config(object):
    """Babel Flask Configuration."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object('4-app.Config')
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def Basic_Flask():
    """Basic-Flask-App."""
    return(render_template('4-index.html'))


@babel.localeselector
def get_locale():
    """Locale from request."""
    URLparameter = request.args.get('locale')
    Languages = app.config['LANGUAGES']
    if URLparameter:
        if URLparameter in Languages:
            return(URLparameter)
    else:
        return(request.accept_languages.best_match(app.config['LANGUAGES']))


if __name__ == "__main__":
    IPaddress = os.getenv("API_HOST", "0.0.0.0")
    app.run(host=IPaddress, port='5000')
