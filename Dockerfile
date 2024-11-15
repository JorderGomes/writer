FROM ubuntu:latest AS build

RUN apt-get update
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python main.py

EXPOSE 5000