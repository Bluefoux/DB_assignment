FROM tiangolo/uwsgi-nginx-flask:python3.11

WORKDIR /app

ADD ./key.pem /root/ssl/
ADD ./cert.pem /root/ssl
ADD ./uwsgi-nginx-entrypoint.sh /
ADD ./entrypoint.sh /

#RUN ["/bin/bash", "-c", "find .","-type f", "-name *.sh", "-exec dos2unix {} 
RUN apt-get update
RUN apt-get install dos2unix
RUN dos2unix /uwsgi-nginx-entrypoint.sh
RUN dos2unix /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/start.sh"]

COPY ./requirements.txt /app/requirements.txt

RUN python -m pip install -r /app/requirements.txt

COPY . /app

ENV DEVELOPMENT=prod

ENV LISTEN_PORT 8500
EXPOSE 8500