drop database if exists proj_db;
create database proj_db;
use proj_db;

ALTER USER 'admin'@'172.19.0.4' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'172.19.0.4' WITH GRANT OPTION;
FLUSH PRIVILEGES;