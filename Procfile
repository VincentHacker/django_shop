web: gunicorn shop.wsgi
worker: celery -A shop worker --beat -S django --l info
