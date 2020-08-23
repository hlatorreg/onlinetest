#!/bin/bash
service mysql start && 
mysql -uroot -e "create database test;  UPDATE mysql.user SET plugin = 'mysql_native_password' WHERE user = 'root' AND host = 'localhost';" &&
gunicorn --bind=0.0.0.0:8000 --workers=4 manage:app 