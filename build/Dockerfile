FROM continuumio/miniconda3:4.8.2

COPY requirements.txt /home

RUN apt-get update && apt-get install git && \
  pip install -r /home/requirements.txt
