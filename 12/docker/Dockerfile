FROM python:3.8.6-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"
RUN apk add postgresql-dev=9.6.10-r0 --repository=http://dl-cdn.alpinelinux.org/alpine/v3.5/main
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ADD . /code/
