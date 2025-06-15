@babel.localeselector
def get_locale() -> str:
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    user = getattr(g, 'user', None)
    if user:
        user_locale = user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES']) or app.config['BABEL_DEFAULT_LOCALE']
