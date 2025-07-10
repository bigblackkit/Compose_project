FROM python:3.12-alpine

# Установка зависимостей (flask и зависимости SSL + DNS)
RUN pip install --no-cache-dir flask

# Создание директории приложения
WORKDIR /app

# Копируем только нужный файл
COPY app.py .

# Указываем порт
EXPOSE 5000

# Команда запуска
CMD ["python", "app.py"]
