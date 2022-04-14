FROM python:3.9-alpine
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ["main.py", "calculator.py", "./"]
CMD ["python", "main.py"]