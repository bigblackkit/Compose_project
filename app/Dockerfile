FROM python:3.12-alpine

# Установка зависимостей (flask и зависимости SSL + DNS)
RUN pip install --no-cache-dir flask gunicorn

# Создание директории приложения
WORKDIR /app

# Копируем только нужный файл
COPY app.py .

# Указываем порт
EXPOSE 5000

# Команда запуска
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
