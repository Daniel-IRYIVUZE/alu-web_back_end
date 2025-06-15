#!/usr/bin/env python3
"""Flask app with i18n and mock user login."""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Union

class Config:
    """App configuration for i18n."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Union[dict, None]:
    """Retrieve user from mock login system using login_as query parameter."""
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None

@app.before_request
def before_request() -> None:
    """Set the global user before each request."""
    g.user = get_user()

@app.route('/')
def index():
    return render_template("5-index.html")
