FROM python:3.13-slim

#set enviroment
ENV PYTHONDONTWRITEBYTECODE 1 # запрещает создавать файлы с кешом внутри контейнера
ENV PYTHONUNBUFFERED 1 # std out std r - запрещает буферизировать все выводы




WORKDIR /usr/scr/dm_rest

COPY ./requirements.txt /usr/scr/requirements.txt
RUN pip install -r /usr/scr/requirements.txt

COPY . /usr/scr/dm_rest




EXPOSE 8000
WORKDIR /usr/scr/dm_rest/s_project


CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]