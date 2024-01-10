FROM tiangolo/uwsgi-nginx-flask:python3.11

WORKDIR /app


COPY ./requirements.txt /app/requirements.txt

RUN python -m pip install -r /app/requirements.txt

COPY . /app

ENV MYSQL_DATABASE=proj_db
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=admin
ENV DEVELOPMENT=prod

ENV LISTEN_PORT 8501
# EXPOSE 8501