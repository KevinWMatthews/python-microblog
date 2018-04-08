from flask import Flask

app = Flask(__name__)

# Import at the bottom of the script to mitigate issues with circular imports
from app import routes
