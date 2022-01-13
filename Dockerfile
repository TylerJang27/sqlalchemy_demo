FROM ubuntu:20.04

# backend system dependencies
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app
COPY . /app

# install backend packages
RUN pip3 install -r requirements.txt


# host site
# CMD python3 app.py
CMD cd /app && python3 app/main.py