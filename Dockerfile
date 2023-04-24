FROM ubuntu:latest

RUN mkdir /app 
WORKDIR /app

RUN apt-get update
RUN apt-get update && apt-get install -y python3

COPY . ./

CMD ["python", "calculadora.py", "test_calculadora.py"]