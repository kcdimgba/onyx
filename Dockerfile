FROM python:3.11 as build
COPY . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
FROM python:3.11-alpine3.17
COPY --from=build /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY . /app
WORKDIR /app
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
