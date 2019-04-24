FROM python:2

COPY requirements.txt .
RUN pip install flake8
RUN pip install -r requirements.txt
COPY settings.py tests.py ./
