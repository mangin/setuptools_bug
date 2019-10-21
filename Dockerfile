FROM python:3.7-alpine3.9

RUN python3.7 -m pip install pip --upgrade
RUN python3.7 -m pip install setuptools==41.4.0

RUN echo -e "import setuptools\nprint('SETUP TOOLS VERSION: setuptools.version.__version__')" | python
RUN python3.7 --version

WORKDIR /project
COPY project /project
RUN python3.7 setup.py test
