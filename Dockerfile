FROM python:3.7-alpine

EXPOSE 5000
WORKDIR /app

COPY . ./
RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
RUN sed -i "s|\("^BIND"=* *\).*|\10.0.0.0|" .env
RUN sed -i "s|\("^LISTEN_PORT"=* *\).*|\15000|" .env

ENTRYPOINT ["python", "app/main.py"]
