
FROM python:3.12-alpine as builder

#
# Create our own venv in /install and install our packages into it.
#
RUN python -m venv /install
ENV PATH="/install/bin:$PATH"

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

#
# Now build our real container, and copy over the site packages only.
# As of this writing, the image size goes from 98.3 MB to 96.2 MB.  
# Not a huge savings, but I'll take it.
#
FROM python:3.12-alpine

RUN apk update && apk add poppler-utils
COPY --from=builder /install/lib/python3.12/site-packages/ /usr/local/lib/python3.12/

COPY bin/entrypoint.sh /

COPY pdf-to-poster.py /app/


ENTRYPOINT [ "/entrypoint.sh" ]


