FROM python:3.5

ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt \
    && groupadd -r flask \
    && useradd -r -g flask flask

COPY . /app
RUN chown -R flask /app

COPY ./entrypoint.sh /entrypoint.sh

RUN sed -i 's/\r//' /entrypoint.sh \
    && chmod +x /entrypoint.sh \
    && chown flask /entrypoint.sh

WORKDIR /app
EXPOSE 5000
ENTRYPOINT ["/entrypoint.sh"]
