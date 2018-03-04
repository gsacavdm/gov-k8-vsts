FROM python:2.7-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ .

EXPOSE 5000
ENTRYPOINT ["python", "/app/main.py"]
