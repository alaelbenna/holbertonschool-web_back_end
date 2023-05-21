#!/usr/bin/env python3
"""New view for Session Authentication."""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def loginFlask() -> str:
    """Flask that handles all login routes for Session Authentication."""
    UserName = request.form.get("email", None)
    UserPassword = request.form.get("password", None)
    # If email is missing
    if UserName is None:
        EmailMissing = jsonify({"error": "email missing"}), 400
        return(EmailMissing)
    # If password is missing
    if UserPassword is None:
        PasswordMissing = jsonify({"error": "password missing"}), 400
        return(PasswordMissing)
    # Search for USER
    FoundUser = User.search({"email": UserName})
    if FoundUser is None:
        return(jsonify({"error": "no user found for this email"}), 404)
    if not FoundUser[0].is_valid_password(UserPassword):
        return(jsonify({"error": "wrong password"}), 401)
    else:  # Create a SESSION ID
        from api.v1.app import auth
        FoundUser = FoundUser[0]
        SessionID = auth.create_session(FoundUser.id)
        DictionaryRepresentation = jsonify(FoundUser.to_json())
        CookieResponse = os.getenv("SESSION_NAME", None)
        DictionaryRepresentation.set_cookie(CookieResponse, SessionID)
        return(DictionaryRepresentation)


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def logoutFlask() -> str:
    """Flask that handles all logout routes for Session Authentication."""
    from api.v1.app import auth
    DeleteIDsession = auth.destroy_session(request)
    if DeleteIDsession:
        abort(404)
        return(False)
    else:
        return(jsonify({}), 200)
