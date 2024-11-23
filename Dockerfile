# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта
COPY . /app/

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Экспонируем порт 8000
EXPOSE 8000

# Команда для запуска приложения
CMD ["gunicorn", "blog_project_v2.wsgi:application", "--bind", "0.0.0.0:8000"]
