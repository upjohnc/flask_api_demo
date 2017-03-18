import sys
import os

for i in ['.']:
    module_path = os.path.abspath(os.path.join(i))
    if module_path not in sys.path:
        sys.path.append(module_path)

from flask import Flask, Blueprint
from flask_rest_service import settings
from flask_rest_service.api.golf.endpoints.course import ns as golf_courses_namespace
from flask_rest_service.api.golf.restplus import api
from flask_rest_service.database import db

app = Flask(__name__)
# db = SQLAlchemy()


def config_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS


def initialize_app(flask_app):
    config_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(golf_courses_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)
    with flask_app.app_context():
        db.create_all()


def main():
    initialize_app(app)
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == '__main__':
    main()

# from flask_rest_service.database import models


# from flask_rest_service.database import db
#
# app = Flask(__name__)
#
#
#
#
