FROM python:3.9-alpine
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY calculator.py .
CMD ["celery", "-A", "calculator", "worker", "--loglevel=INFO"]