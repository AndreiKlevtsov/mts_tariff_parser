# mts_tariff_parser

# Foodgram

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

## Tecnhologies

- Python 3.11
- Django 4.2.3
- Django REST framework 3.14
- Nginx
- Docker
- Postgres

## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone git@github.com:AndreiKlevtsov/mts_tariff_parser.git
```
```
cd mts_tariff_parser


```

## Для работы с удаленным сервером:
* Выполните вход на свой удаленный сервер

* Установите docker на сервер:
```
sudo apt install docker.io 
```
* Установите docker-compose на сервер:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
* Локально отредактируйте файл gateway/nginx.conf и в строке server_name впишите свой IP и/или доменное имя.
* Скопируйте файлы docker-compose.yml и nginx.conf из директории gateway на сервер:
```
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp nginx.conf <username>@<host>:/home/<username>/nginx.conf
```

* Cоздайте .env файл и впишите:
```
DB_ENGINE=<django.db.backends.postgresql>
DB_NAME=<name_postgres>
DB_USER=<user+postgres>
DB_PASSWORD=<password_postgres>
DB_HOST=<db>
DB_PORT=<5432>
SECRET_KEY=<secret key проекта django>
```

- Проект будет доступен по вашему IP
