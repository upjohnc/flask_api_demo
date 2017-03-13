#!/usr/bin/env python

from migrate.versioning import api
from flask import Flask
from flask_rest_service.settings import SQLALCHEMY_DATABASE_URI
from flask_rest_service.settings import SQLALCHEMY_MIGRATE_REPO
from flask_sqlalchemy import SQLAlchemy
from flask_rest_service import settings
import os
from flask_rest_service.app import app

# app = Flask(__name__)
db = SQLAlchemy(app)


app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

db.create_all()

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
