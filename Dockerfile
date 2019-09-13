FROM python:3.7-stretch

RUN pip install -U pip
RUN pip install git+https://github.com/miurahr/pykakasi
WORKDIR /usr/src/

ENTRYPOINT ["/usr/local/bin/python3","kakasi_test.py"]
