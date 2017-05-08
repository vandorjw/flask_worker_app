# -*- coding: utf-8 -*-
"""Public section"""
import time
from random import randint
from flask import Blueprint

blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET', 'POST'])
def home():
    return "Home"


@blueprint.route('/random', methods=['GET', ])
def random_request():
    sleep_time = randint(60, 300)
    time.sleep(sleep_time)
    return "do work for {}".format(sleep_time)

