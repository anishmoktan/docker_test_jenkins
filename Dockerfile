FROM debian:latest

RUN apt-get update 
RUN apt-get install -y python3 

COPY ./Test.py /usr/src/app/Test.py

WORKDIR /usr/src/app/
