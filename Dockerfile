FROM python:3.8.7-buster

RUN apt-get update \
    && apt-get install -y mitmproxy
RUN pip install pytest requests assertpy mitmproxy

RUN mkdir demo
COPY proxyscript.py requirement.txt tests.py demo/

#    && source venv/bin/activate \
#    && python -m venv venv \
#RUN cd demo \
#    && pip install -r requirement.txt

EXPOSE 8080
ENTRYPOINT pytest -q demo/tests.py
