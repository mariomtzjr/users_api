# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim-buster

EXPOSE 8000
ENV LISTEN_PORT=8000
ENV FLASK_APP=main:app
ENV FLASK_ENV=development
ENV APP_SETTINGS_MODULE=config.default.DevelopmentConfig

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
CMD python ./scripts/seed.py && python ./manage.py db init && python ./manage.py db migrate && python ./manage.py db upgrade && python ./manage.py runserver -p 8000 --reload