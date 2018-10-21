# Microblog

Follow the steps in Miguel Grinberg's Flask Mega-tutorial to create a microblog.

## Getting started

### Install

Clone this project.
```
$ git@github.com:KevinWMatthews/python-microblog.git
```

Create and activate a virtual environment.
```
$ cd <microblog>
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

Install required Python packages into the virtual environment.
```
$ pip install -r requirements.txt
```

### Run

I'm using a `.flaskenv` and `.env` file that is parsed by `python-dotenv`.
This sets the `FLASK_APP` and `FLASK_ENV` environment variables for us.
Be sure you don't set them yourself! The command line/current environment takes precedence.

Run using simply:
```
$ flask run
```

To run the application in debug mode, set another file:
```
$ vim .env
FLASK_ENV=development
```

Or set another environment variable:
```
# Flask 1.0
$ export FLASK_ENV=development
# defaults to 'production', I believe

# Flask 0.12
$ export FLASK_DEBUG=1
```


### Database migration

Set up migration stuff (be sure the environment variable `FLASK_APP` is set):
```
$ flask db init
```

Generate the migration scripts:
```
$ flask db migrate
```

Run the migration:
```
$ flask db upgrade
# or to revert
$ flask db downgrade
```

### Experimentation

If you need a shell into your current flask environment, simply run:
```
$ flask shell
```
The shell context is configurable in `microblog.py`.


### Mail Server

You can run a dummy mail server locally using:
```
$ python -m smtpd -n -c DebuggingServer localhost:8025
```

This will run a smtp server on your machine. It will receive e-mails and
print them to the console.
