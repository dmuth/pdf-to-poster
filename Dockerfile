
FROM python:3.12-alpine

RUN python -m pip install --upgrade pip

RUN apk update && apk add poppler-utils

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY bin/entrypoint.sh /

COPY pdf-to-poster.py /app

ENTRYPOINT [ "/entrypoint.sh" ]


