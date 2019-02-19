FROM python:3.5-slim

ADD drf_starter /usr/app/drf_starter/
ADD manage.py requirements.* /usr/app/
WORKDIR /usr/app
RUN pip install -r requirements.txt -r requirements.deploy.txt

ENTRYPOINT ["/usr/local/bin/gunicorn", "drf_starter.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
