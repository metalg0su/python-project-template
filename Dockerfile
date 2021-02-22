FROM python:3.8

COPY . /app
WORKDIR /app

EXPOSE 80

RUN pip install -e .
CMD ["echo", "dd"]

