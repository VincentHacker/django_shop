web: gunicorn shop.wsgi
worker: celery -A shop worker --beat -l info -S django 
