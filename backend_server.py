"""
    Setup the application api server
"""

from flask import Flask
from flask_restful import Api as RESTfulAPI

from resources import SimpleResource


def _init_app(app):
    rest_api = RESTfulAPI(app, catch_all_404s=True)
    rest_api.add_resource(SimpleResource, '/api/simple')
    return app

def _get_all():
    app = Flask(__name__)
    with app.app_context():
        _init_app(app)

    return app

# Produce initialised app.
simple_app = _get_all()

if __name__ == '__main__':
    simple_app.run('127.0.0.1',debug=True)

