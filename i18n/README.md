# Flask i18n App

This project is part of the Holberton School curriculum and demonstrates how to internationalize a Flask web application using Flask-Babel.

## Features

✅ Supports multiple languages (`en`, `fr`)  
✅ Locale selection via:
- URL parameters (`?locale=fr`)
- User preferences (simulated login)
- Browser headers (`Accept-Language`)

✅ Timezone selection via:
- URL parameters (`?timezone=Europe/Paris`)
- User preferences
- Fallback to default (`UTC`)

✅ User simulation using `login_as` query param  
✅ Translations using Jinja2 and `.po` files

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install Flask Flask-Babel pytz
````

2. Compile translations:

   ```bash
   pybabel extract -F babel.cfg -o messages.pot .
   pybabel init -i messages.pot -d translations -l en
   pybabel init -i messages.pot -d translations -l fr
   # (Edit .po files for both languages)
   pybabel compile -d translations
   ```

3. Run the Flask app:

   ```bash
   export FLASK_APP=7-app.py
   flask run
   ```

## Usage

Access the app in your browser:

```
http://localhost:5000
```

To test localization and timezone:

* `http://localhost:5000/?locale=fr`
* `http://localhost:5000/?login_as=1`
* `http://localhost:5000/?login_as=2&timezone=US/Central`

## Author

Daniel Iryivuze 

```