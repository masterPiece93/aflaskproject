# app creation
import os
from flask import Flask
from routes import api_routes


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    routes = api_routes(app)
    routes.v1()
    routes.v2()
    return app
