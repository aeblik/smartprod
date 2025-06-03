FROM python:3.10-slim

WORKDIR /app

# Copy requirements from project root
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app folder contents into /app
COPY app/ .

CMD ["python", "app.py"]
