FROM python:3.7.3-slim-stretch

WORKDIR /code

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    git \
    libc-dev \
    pkg-config \
    libsecp256k1-dev \
    rabbitmq-server \
    vim-tiny \
    lsof \
    && rm -rf /var/lib/apt/lists/*
    


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

ENV FLASK_APP webapp/main.py
ENV FLASK_RUN_HOST 0.0.0.0

CMD ["flask", "run"]