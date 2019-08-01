FROM python:latest

ADD ./requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -q -r /tmp/requirements.txt

ADD ./ /opt/app
WORKDIR /opt/app

RUN adduser --disabled-password --gecos '' superuser
USER superuser

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]