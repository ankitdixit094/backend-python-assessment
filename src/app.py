from __future__ import absolute_import, unicode_literals
from flask import Flask
import os
import logging.config
import mongoengine
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from celery import Celery
from bson import ObjectId, json_util
import json

application = Flask(os.environ.get("APPLICATION_NAME"))
SETTINGS_FILE = os.environ.get("SETTINGS_FILE", "settings.local_settings")

application.config.from_object(SETTINGS_FILE)

db = MongoEngine(application)
jwt = JWTManager(application)

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_SETTINGS']['celery_result_backend'],
        broker=app.config['CELERY_SETTINGS']['celery_broker_url'],
    )
    celery.conf.update(app.config)
    return celery

celery = make_celery(application)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj)

application.json_encoder = CustomJSONEncoder

with application.app_context():
    # this loads all the views with the app context
    # this is also helpful when the views import other
    # modules, this will load everything under the application
    # context and then one can use the current_app configuration
    # parameters
    from apis.urls import all_urls
    from scripts import ALL_CLI_COMMANDS

    for cli_name, cli_command in ALL_CLI_COMMANDS.items():
        application.cli.add_command(cli_command, name=cli_name)


# Adding all the url rules in the api application
for url, view, methods, _ in all_urls:
    application.add_url_rule(url, view_func=view, methods=methods)


logging.config.dictConfig(application.config["LOGGING"])
