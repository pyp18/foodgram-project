FROM python:3.8.5

RUN pip install --upgrade pip

RUN mkdir /code

COPY requirements.txt /code

RUN pip install -r /code/requirements.txt

RUN pip install https://github.com/darklow/django-suit/tarball/v2

COPY . /code

WORKDIR /code

RUN python --version; pip --version

CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000