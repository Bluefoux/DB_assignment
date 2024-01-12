FROM mysql:8.0.35

RUN chown -R mysql:root /var/lib/mysql/


MAINTAINER admin

ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_ROOT_PASSWORD

ENV MYSQL_DATABASE=proj_db
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=admin
ENV MYSQL_ROOT_PASSWORD=admin

ADD sql_data/tables.sql /etc/mysql/query_data/tables.sql

RUN cp /etc/mysql/query_data/tables.sql /docker-entrypoint-initdb.d

# EXPOSE 3306