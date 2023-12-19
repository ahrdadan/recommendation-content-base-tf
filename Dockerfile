FROM python:3.11

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "src.main:app", "--reload"]
