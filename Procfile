release : python3 manage.py migrate
release : python3 manage.py collectstatic
web: gunicorn config.wsgi --log-file - 
worker: python worker.py