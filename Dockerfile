FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install toolz
RUN pip3 install setuptools
RUN pip3 install sidekick
RUN pip3 install pytest~=5.0
RUN pip3 install markupsafe
RUN pip3 install -r requirements.txt
ADD . /code/
EXPOSE 8000