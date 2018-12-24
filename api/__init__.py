"""
App is created here"""

import os
from flask import Flask
from instance.config import app_config
from api.v1.auth.users_view import v1


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.register_blueprint(v1)
    
    return app 