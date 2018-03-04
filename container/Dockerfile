FROM tiangolo/uwsgi-nginx-flask:python3.6

ADD /src /app
EXPOSE 5000

ENTRYPOINT ["python", "/app/main.py"]
