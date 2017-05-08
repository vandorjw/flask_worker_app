# gunicorn.py
bind = '0.0.0.0:5000'
backlog = 512
workers = 10
worker_class = 'gthread'
timeout = 600
