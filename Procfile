release : python3 manage.py migrate
web: gunicorn config.wsgi
worker: python worker.py