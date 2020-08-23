FROM python:3.7.3-slim
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV TZ=America/Santiago
ENV FLASK_ENV=development
ENV FLASK_APP=manage.py
ENV APP_SETTINGS=main.configs.DevelopmentConfig
ENV FLASK_DEBUG=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY=abretesesamo

RUN apt-get update
RUN apt-get install curl -y
RUN apt-get install gcc -y
RUN apt-get install default-libmysqlclient-dev -y
RUN apt-get install mysql-server -y

ENV USER=root
ENV HOST=127.0.0.1
ENV DATABASE=test
ENV PASS="" 

COPY ./src /usr/src/app

RUN pip install -e .

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
