from flask import Flask

app = Flask(__name__)

from app import routes, models  # Import routes and models to register them with the app