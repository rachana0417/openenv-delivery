FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn requests

EXPOSE 7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]