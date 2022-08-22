from flask_restful import Api
from flask import Blueprint, Flask
import json

from .config import Config

apiv1_bp = Blueprint(name='apiv1_bp', import_name=__name__, url_prefix='/api/v1')
apiv1 = Api(apiv1_bp)

from . import resource

def create_app(config_file=None):
    app = Flask(__name__)
    if config_file is not None:
        app.config.from_file(config_file, load=json.load) 
    else:
        app.config.from_object(Config)
    
    app.register_blueprint(apiv1_bp) # register /api/v1 blueprint to main app
    
    return app
