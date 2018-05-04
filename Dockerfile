FROM python:2.7.14-slim-jessie
ENV INITSYSTEM on

RUN apt-get update && apt-get install -y build-essential libffi-dev freetds-dev libpq-dev libmysqlclient-dev python3-dev python3-pip npm nodejs-legacy && \
       npm install -g configurable-http-proxy && \
       pip install --upgrade pip cython setuptools && \
       pip3 install --upgrade pip setuptools cython && \
       mkdir -p /etc/jupyterhub
RUN    pip3 install --upgrade notebook jupyterhub jupyterlab && \
       jupyter serverextension enable --py jupyterlab --sys-prefix
COPY ./jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py


WORKDIR /
EXPOSE 80
CMD jupyterhub --port=80
