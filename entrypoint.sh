#!/bin/bash
service mysql start && 
mysql -uroot -e "create database test;  UPDATE mysql.user SET plugin = 'mysql_native_password' WHERE user = 'root' AND host = 'localhost';" &&
flask db upgrade && 
flask run --host=0.0.0.0 --port=8000
