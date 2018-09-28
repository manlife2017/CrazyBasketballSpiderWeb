# -*- coding:utf-8 -*-
from flask import Blueprint

simple_page = Blueprint('', __name__,template_folder='templates')


@simple_page.route('/')
def hello_world():
    return 'Hello World!'


# @app.route("/spider/start")
# def spider_start():
#     params = {
#         "project":"zouwei_spider",
#         "spider":"youku"
#     }
#     res = requests.post("http://localhost:6800/schedule.json",data=params)
#     return jsonify(json.loads(res.text))


# @app.route("/spider/start")
# def spider_stop():
#     return "spider stop"