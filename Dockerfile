FROM python:3.11

RUN pip install -r requirements.txt

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "src.main:app", "--reload"]

EXPOSE 8000