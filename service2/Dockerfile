FROM python:3.8

COPY ./requirements.txt . 

RUN pip3 install -r requirements.txt

COPY . . 

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "app:app"]