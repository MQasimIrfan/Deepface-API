from flask import Flask
from flask_cors import CORS
from deepface import DeepFace
from deepface.api.src.modules.core.routes import blueprint
from deepface.commons.logger import Logger
import os

logger = Logger()

def create_app():
    app = Flask(__name__)

    # Allow CORS for only your frontend
    CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://your-react-app.com"]}})

    app.register_blueprint(blueprint)
    logger.info(f"Welcome to DeepFace API v{DeepFace.__version__}!")
    return app

if __name__ == "__main__":
    deepface_app = create_app()
    deepface_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
