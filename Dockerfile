FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

COPY . .

CMD ["pytest"]
