FROM python:3.7

WORKDIR /home/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app app

COPY migrations migrations

COPY config.py  ./

EXPOSE 5000

ENV FLASK_ENV development

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]


