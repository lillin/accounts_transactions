FROM python:3.6
ENV PYTHONUNBUFFERED 1

WORKDIR /accounts_transactions

ADD requirements.txt /accounts_transactions
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ADD . /accounts_transactions
