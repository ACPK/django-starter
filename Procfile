web: gunicorn project.wsgi --log-file=- --log-level=debug
worker: celery worker --app=project.settings.celery:app