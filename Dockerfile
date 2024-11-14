# Используем официальный образ Python в качестве основы
FROM python:3.13-slim

# Устанавливаем Pandas
RUN pip install pandas

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы в контейнер
COPY app.py /app/
COPY data.csv /app/

# Указываем, какую команду запускать
CMD ["python", "app.py"]
