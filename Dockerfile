From python:3.9

RUN mkdir /project
WORKDIR /project

COPY requirements.txt /project/
RUN pip install -r requirements.txt
COPY . /project/


