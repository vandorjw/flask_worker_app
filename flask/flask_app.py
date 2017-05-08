# -*- coding: utf-8 -*-
"""Create an application instance."""
from app.app import create_app
from app.config import Config

app = create_app(Config)
