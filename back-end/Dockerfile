FROM python:3
ENV PYTHONUNBUFFERED=1
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/

