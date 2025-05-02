FROM python:3.10-slim

WORKDIR /app

# Copy requirements from the actual api folder
COPY ./api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire api app
COPY ./api /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]