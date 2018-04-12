# Microblog

Follow the steps in Miguel Grinberg's Flask Mega-tutorial to create a microblog.

## Getting started

### Installation
Clone this project.
Create and activate a virtual environment.
```
virtualenv -p python3 venv
source venv/bin/activate
```

Install required Python packages into the virtual environment.
```
pip install -r requirements.txt
```

### Running the application
Use flask to run the application:
```
export FLASK_APP=microblog.py
flask run
```

To run the application in debug mode,
```
export FLASK_DEBUG=1
```
