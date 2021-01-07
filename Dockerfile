FROM python:3.8.7-buster

RUN apt-get update \
    && apt-get install -y mitmproxy

RUN mkdir demo
COPY proxyscript.py requirement.txt demo/

RUN cd demo \
    && python -m venv venv \
    && source venv/bin/activate \
    && pip install -r requirement.txt
