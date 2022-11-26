FROM python:3.11.0-alpine3.15

WORKDIR /app

COPY ./requirements.txt ./

RUN apk update \
    && apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps gcc musl-dev