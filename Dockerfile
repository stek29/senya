FROM python:3-slim-buster
RUN useradd -ms /bin/bash app

RUN apt-get -y update \
    && apt-get install -y \
        build-essential cmake pkg-config \
    && pip install dlib>=19.3.0 \
    && apt-get remove -y \
        build-essential cmake pkg-config \
    && apt-get clean && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

RUN pip install face_recognition_models

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

USER app
COPY . .

ENTRYPOINT [ "docker/start.sh" ]
