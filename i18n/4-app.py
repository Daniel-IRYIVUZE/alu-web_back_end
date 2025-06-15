#!/usr/bin/env python3
"""Flask app forcing locale from URL."""

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    """Configuration for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index():
    return render_template("4-index.html")

@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])
