#!/bin/bash
set -e
cmd="$@"

if [ -z "$REDIS_URL" ]; then
    export REDIS_URL=redis://redis:6379
fi

/usr/local/bin/gunicorn --config=gunicorn_config.py flask_app:app
