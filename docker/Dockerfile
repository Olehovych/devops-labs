FROM python:3.12-slim

# Встановлюємо Flask
RUN pip install flask

# Копіюємо код у контейнер
WORKDIR /app
COPY app.py .

# Запускаємо Flask
CMD ["python", "app.py"]
