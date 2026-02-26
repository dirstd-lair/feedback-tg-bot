FROM python:3.13.2

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN mkdir -p /app/database

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m myuser && chown -R myuser /app
USER myuser

CMD ["python", "main.py"]
