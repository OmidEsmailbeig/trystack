from flask import Flask
from .config import Config
import json

def create_app(config_file=None):
    app = Flask(__name__)
    if config_file is not None:
        app.config.from_file(config_file, load=json.load) 
    else:
        app.config.from_object(Config)
    
    return app
