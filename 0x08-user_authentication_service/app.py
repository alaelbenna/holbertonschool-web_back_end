#!/usr/bin/env python3
"""Basic-Flask-App."""

from flask import Flask, jsonify, request, abort, redirect, url_for
from sqlalchemy.orm.exc import NoResultFound

from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """Welcome-to-Flask."""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def emailCheck() -> str:
    """Email-Verification."""
    form_data = request.form
    if "email" not in form_data:
        return (jsonify({"message": "email required"}), 400)
    elif "password" not in form_data:
        return (jsonify({"message": "password required"}), 400)
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        try:
            new_user = AUTH.register_user(email, password)
            return (jsonify({
                "email": new_user.email,
                "message": "user created"
            }))
        except ValueError:
            return (jsonify({"message": "email already registered"}), 400)


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def sign_in():
    """Username credentials."""
    if "email" in request.form.keys() and "password" in request.form.keys():
        try:
            username = request.form['email']
            passwd = request.form['password']
            if AUTH.valid_login(username, passwd):
                session_id = AUTH.create_session(username)
                response = {
                    "email": "{}".format(username),
                    "message": "logged in"
                }
                response = jsonify(response)
                response.set_cookie("session_id", session_id)
                return (response)
            else:
                abort(401)
        except NoResultFound:
            abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def sign_out() -> None:
    """Password Credentials."""
    session_id = request.cookies.get('session_id')
    if session_id:
        password = AUTH.get_user_from_session_id(session_id)
        if password:
            AUTH.destroy_session(password.id)
            return (redirect(url_for('index')))
    else:
        abort(403)


@app.route("/profile", methods=['GET'], strict_slashes=False)
def get_profile() -> str:
    """Find users account."""
    sessionid = request.cookies.get('session_id', None)
    if sessionid is None:
        abort(403)
    username = AUTH.get_user_from_session_id(sessionid)
    if username is None:
        abort(403)
    return (jsonify({"email": username.split(":")[0]}))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
