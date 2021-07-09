FROM python:3.8.8

WORKDIR /home/

RUN git clone https://github.com/lee-JunR/accounteapi

WORKDIR /home/accountapi/

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]