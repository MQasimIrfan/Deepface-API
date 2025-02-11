# # 3rd parth dependencies
# from flask import Flask
# from flask_cors import CORS

# # project dependencies
# from deepface import DeepFace
# from deepface.api.src.modules.core.routes import blueprint
# from deepface.commons.logger import Logger

# logger = Logger()


# def create_app():
#     app = Flask(__name__)
#     CORS(app)  
#     app.register_blueprint(blueprint)
#     logger.info(f"Welcome to DeepFace API v{DeepFace.__version__}!")
#     return app

from flask import Flask
from flask_cors import CORS

# Import DeepFace-related dependencies
from deepface import DeepFace
from deepface.api.src.modules.core.routes import blueprint
from deepface.commons.logger import Logger

logger = Logger()

def create_app():
    app = Flask(__name__)
    
    # Allow specific origins instead of '*'
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    @app.after_request
    def add_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        return response

    app.register_blueprint(blueprint)
    logger.info(f"Welcome to DeepFace API v{DeepFace.__version__}!")
    return app

