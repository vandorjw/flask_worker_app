# -*- coding: utf-8 -*-
"""Public section"""
from datetime import datetime
import json
import time
from random import randint
from flask import Blueprint
from app.sqs import submit_to_sqs

blueprint = Blueprint('public', __name__)


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    return "Home"


@blueprint.route('/submit', methods=['GET', ])
def submit_to_queue():
    from flask_app import app
    timestamp = datetime.now().timestamp()
    payload = {'data': 'test', 'timestamp': timestamp, }
    try:
        result = submit_to_sqs(app.config['SQS_REGION'], app.config['SQS_QUEUE_NAME'], json.dumps(payload))
        print(result)
        return "success"
    except Exception as err:
        short_error = err.args[0]
        log_msg = "Failed submit to queue due to {}".format(short_error)
        print(log_msg)
        return "failure"


@blueprint.route('/random', methods=['GET', ])
def random_request():
    sleep_time = randint(60, 300)
    time.sleep(sleep_time)
    return "do work for {}".format(sleep_time)
