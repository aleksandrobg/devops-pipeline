FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]
