# -*- coding: utf-8 -*-
"""Public section"""
from decimal import Decimal
from datetime import datetime
import json
import os
import time
from random import randint
from flask import Blueprint
from app.sqs import submit_to_sqs

blueprint = Blueprint('public', __name__)


def bellardBig(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k/(1024**k))*( Decimal(256)/(10*k+1) + Decimal(1)/(10*k+9) - Decimal(64)/(10*k+3) - Decimal(32)/(4*k+1) - Decimal(4)/(10*k+5) - Decimal(4)/(10*k+7) -Decimal(1)/(4*k+3))
        k += 1
    pi = pi * 1/(2**6)
    return pi


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


@blueprint.route('/random', methods=['POST', ])
def random_request():
    min_val = os.getenv('PI_MIN_VALUE', 1000)
    max_val = os.getenv('PI_MAX_VALUE', 4000)
    try:
        min_val = int(min_val)
        max_val = int(max_val)
    except:
        min_val = 1000
        max_val = 4000

    pid = os.getpid()
    pi_digits = randint(min_val, max_val)
    bellardBig(pi_digits)
    print("Worker {} calculated pi to {} decimal places".format(pid, pi_digits))
    return "Worker {} calculated pi to {} decimal places".format(pid, pi_digits)
