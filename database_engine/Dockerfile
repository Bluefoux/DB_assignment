FROM tiangolo/uwsgi-nginx-flask:python3.11



WORKDIR /app

# Install wait-for-it
ADD https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Copy the entry point script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./requirements.txt /app/requirements.txt

RUN python -m pip install -r /app/requirements.txt

COPY . /app

ENV MYSQL_DATABASE=proj_db
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=admin
ENV DEVELOPMENT=prod

# Set the entry point
ENTRYPOINT ["/entrypoint.sh"]

ENV LISTEN_PORT 8501
EXPOSE 8501
