from flask import Blueprint, Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import json

from .config import Config

db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()

apiv1_bp = Blueprint(
        name='apiv1_bp',
        import_name=__name__,
        url_prefix='/api/v1'
    )
apiv1 = Api(apiv1_bp)

from . import resource


def create_app(config_file=None):
    app = Flask(__name__)
    if config_file is not None:
        app.config.from_file(config_file, load=json.load)
    else:
        app.config.from_object(Config)

    print(Config.DEBUG)

    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)

    app.register_blueprint(apiv1_bp)  # register /api/v1 blueprint to main app

    return app
