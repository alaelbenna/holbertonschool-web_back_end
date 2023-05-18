#!/usr/bin/env python3
"""This module contains task 3"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """Configuration class for templates"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """get_user - gets user from dict"""
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """before request - finds user for use"""
    user = get_user()
    print("user", user)
    g.user = user


@babel.localeselector
def get_locale():
    """lang selector based on location"""
    lang = None
    if g.user is not None:
        lang = g.user.get('locale')
    if request.args.get('locale'):
        lang = request.args.get('locale')

    if lang is not None:
        if lang == 'en':
            return Config.LANGUAGES[0]
        if lang == 'fr':
            return Config.LANGUAGES[1]
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def hello_world():
    """This function renders a template"""
    print("g ->", type(g.user))
    username = g.user
    return render_template('6-index.html', username=g.user)
