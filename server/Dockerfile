FROM python:3.10 as python-base
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    SERVER_PORT=8000 

FROM python-base as runtime
WORKDIR /lab/server

RUN apt-get update \
    && apt-get install -y \
        netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
COPY ./films ./films
COPY ./config ./config
RUN pip install -r ./config/requirements.txt

EXPOSE $SERVER_PORT
RUN chmod +x ./config/entrypoint.sh

ENTRYPOINT ["./config/entrypoint.sh"]