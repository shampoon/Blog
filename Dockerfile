FROM python:3.9


RUN apt update; apt install -y npm

ADD requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt; rm /tmp/requirements.txt

COPY . /opt/app
WORKDIR /opt/app

EXPOSE 8000
VOLUME /data/
ENV DB_PATH '/data/db.sqlite3'

CMD npm install; \
    ./manage.py migrate; \
    ./manage.py runserver 0.0.0.0:8000