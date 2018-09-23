# -*-config:utf-8 -*
import requests
import json
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/spider/start")
def spider_start():
    params = {
        "project":"zouwei_spider",
        "spider":"youku"
    }
    res = requests.post("http://localhost:6800/schedule.json",data=params)
    return jsonify(json.loads(res.text))


@app.route("/spider/start")
def spider_stop():
    return "spider stop"

if __name__ == '__main__':
    app.run()
