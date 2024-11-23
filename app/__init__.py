from flask import Flask
from .routes import main_routes  # Import the routes defined in routes.py

# Function to initialize the app
def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_pyfile('../config.py')

    # Register the routes
    app.register_blueprint(main_routes)

    return app

