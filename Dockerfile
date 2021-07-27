FROM python
WORKDIR /usr/src/app
RUN apt-get update
RUN apt-get install -y postgresql-dev
RUN apt-get install -y gcc
RUN apt-get install -y python3-dev
RUN apt-get install -y musl-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . /usr/src

