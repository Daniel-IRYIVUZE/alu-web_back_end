import pytz
from pytz.exceptions import UnknownTimeZoneError

@babel.timezoneselector
def get_timezone() -> str:
    """Select a valid timezone."""
    tz_param = request.args.get("timezone", None)
    if tz_param:
        try:
            return pytz.timezone(tz_param).zone
        except UnknownTimeZoneError:
            pass

    user = g.get("user", None)
    if user:
        try:
            return pytz.timezone(user.get("timezone")).zone
        except UnknownTimeZoneError:
            pass

    return app.config["BABEL_DEFAULT_TIMEZONE"]
