FROM python
WORKDIR /usr/src/kvartirka
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .

