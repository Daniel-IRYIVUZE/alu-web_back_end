#!/usr/bin/env python3
"""Flask app with Babel and template translation."""
from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index():
    return render_template("3-index.html")

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])
