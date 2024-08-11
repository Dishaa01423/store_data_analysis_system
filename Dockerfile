FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH=/app:$PYTHONPATH
ENV PORT=8000
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
