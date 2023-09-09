FROM python:3.11
MAINTAINER Donghee Han "hdh7485l@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
