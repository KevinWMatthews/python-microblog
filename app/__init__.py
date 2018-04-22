from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import at the bottom of the script to mitigate issues with circular imports
from app import routes
