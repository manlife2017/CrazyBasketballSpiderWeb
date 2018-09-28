# -*-coding:utf-8 -*
import requests
import json
from flask import Flask, jsonify
from config import config
from application.db import db
from controller.index_controller import simple_page
app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(simple_page)
db.init_app(app)


if __name__ == '__main__':
    app.run()
