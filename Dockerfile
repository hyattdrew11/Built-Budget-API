FROM python:3.7

WORKDIR /home/app

RUN apt update && \
    apt install -y netcat-openbsd


COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app app

COPY migrations migrations

COPY config.py  ./

COPY startup.sh  ./

EXPOSE 5000

ENV FLASK_ENV development

RUN chmod +x startup.sh

CMD ["/bin/bash", "/home/app/startup.sh"]



