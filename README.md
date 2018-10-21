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

Set the flask application in the environment:
```
$ export FLASK_APP=microblog.py
```

Run using simply:
```
$ flask run
```

To run the application in debug mode, set another environment variable:
```
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
