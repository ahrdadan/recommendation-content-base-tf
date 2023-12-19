FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash", "-c", "cd src && uvicorn main:app --host 0.0.0.0 --port 80"]

EXPOSE 80