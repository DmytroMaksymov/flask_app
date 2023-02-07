FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/cache/apt
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python3 app.py
