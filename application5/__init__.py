from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

application = Flask(__name__)
application.config.from_object(Config)

db = MongoEngine()
db.init_app(application)

from application5 import routes