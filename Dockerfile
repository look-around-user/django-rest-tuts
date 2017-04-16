FROM python:3.6.1

RUN pip install django

WORKDIR /code

RUN pip install djangorestframework
RUN pip install pygments


