FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# USER me

WORKDIR /back-sample

COPY Pipfile Pipfile.lock /back-sample/

RUN apk add --update --no-cache build-base libffi-dev postgresql-dev && \
    pip3 install pipenv && \
    pipenv install --system

# COPY . /backend