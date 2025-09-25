# DevOps Labs

Репозиторій для виконання лабораторних робіт з дисципліни **DevOps**.

## Структура проєкту

ansible/ - файли для автоматизації розгортання (Ansible)
terraform/ - інфраструктура як код (Terraform)
docker/ - Dockerfile та конфігурації контейнерів

## Використовуваний сервіс

В якості сервісу використовується простий Flask-додаток, який повертає `Hello, DevOps!`.

## Команди для запуску Docker контейнера

1. Створення образу:

   ```bash
   docker build -t flask-app docker/

   ```

2. docker run -p 5000:5000 flask-app

3. http://localhost:5000
