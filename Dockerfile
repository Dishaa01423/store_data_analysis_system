FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY data/ ./data/
COPY tests/ ./tests/

CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "src.main:app"]
