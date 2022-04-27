# start by pulling the python image
FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app

# switch working directory
WORKDIR /app

# copy every content from the local file to the image
COPY . /app


# install the dependencies and packages in the requirements file
RUN apk update \
    && apk add build-base

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# configure the container to run in an executed manner
CMD python ./scripts/seed.py && python ./manage.py db init && python ./manage.py db migrate && python ./manage.py db upgrade && python ./manage.py runserver -p 8000

