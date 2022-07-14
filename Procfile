web: gunicorn shop.wsgi
worker: celery -A cfehome worker --beat -S django --l info
