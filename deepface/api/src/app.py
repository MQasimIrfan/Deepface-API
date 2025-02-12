from flask import Flask
from flask_cors import CORS
from deepface import DeepFace
from deepface.api.src.modules.core.routes import blueprint
from deepface.commons.logger import Logger

logger = Logger()

def create_app():
    app = Flask(__name__)

    # Allow CORS for all domains
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.register_blueprint(blueprint)
    logger.info(f"Welcome to DeepFace API v{DeepFace.__version__}!")
    return app
