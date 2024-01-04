FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y gnupg curl
RUN curl -fsSL https://www.mongodb.org/static/pgp/server-5.0.asc | gpg --dearmor -o /usr/share/keyrings/mongodb-archive-keyring.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/mongodb-archive-keyring.gpg] http://repo.mongodb.org/apt/debian buster/mongodb-org/5.0 main" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list

RUN apt-get update && apt-get install -y mongodb-org-tools && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app 

COPY requirements.txt ./
COPY main.py .

RUN pip install fastapi uvicorn pymongo

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
