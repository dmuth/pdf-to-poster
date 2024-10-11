
FROM python:3.12

RUN python -m pip install --upgrade pip

#COPY requirements.txt /app/requirements.txt
#RUN pip install -r /app/requirements.txt


COPY bin/entrypoint.sh /

#COPY pdf-to-poster.py /app

ENTRYPOINT [ "/entrypoint.sh" ]


