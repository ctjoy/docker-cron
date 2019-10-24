FROM kennethreitz/pipenv

RUN apt-get update && apt-get -y install vim

COPY . /app
RUN chmod 755 /app/main.py

CMD ["python3", "/app/main.py"]
