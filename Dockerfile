#cd .. on host machine
FROM python:3.8-alpine

WORKDIR /app

RUN pip install flask==2.2.2 waitress==2.1.2 Werkzeug==2.2.2

COPY ./keygen-plugins/ /app

COPY ./keygen-core/ /app

CMD ["python",  "server.py"]