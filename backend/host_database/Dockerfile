FROM mysql:8.0.34

RUN chown -R mysql:root /var/lib/mysql/


MAINTAINER admin

ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_ROOT_PASSWORD

ENV MYSQL_DATABASE=comp_db
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=root
ENV MYSQL_ROOT_PASSWORD=root

ADD sql_data/tables.sql /etc/mysql/query_data/tables.sql
#ADD sql_data/insert.sql /etc/mysql/query_data/insert.sql
#ADD sql_data/procedures.sql /etc/mysql/query_data/procedures.sql

RUN cp /etc/mysql/query_data/tables.sql /docker-entrypoint-initdb.d
#RUN cp /etc/mysql/query_data/insert.sql /docker-entrypoint-initdb.d
#RUN cp /etc/mysql/query_data/procedures.sql /docker-entrypoint-initdb.d

EXPOSE 3306