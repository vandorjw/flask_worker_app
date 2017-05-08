# -*- coding: utf-8 -*-
"""Public section"""
from datetime import datetime
import time
from random import randint
from flask import Blueprint
from flask import app
from flask.app import sqs

blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET', 'POST'])
def home():
    return "Home"


@blueprint.route('/submit', method=['GET', ])
def submit_to_queue():
    timestamp = datetime.now().timestamp()
    payload = {'data': 'test', 'timestamp': timestamp, }
    try:
        submit_to_sqs(app.config['SQS_REGION'], app.config['SQS_QUEUE_NAME'], json.dumps(payload))
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

