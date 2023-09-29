# USERS

Проект на Django разработан для предоставления функциональности регистрации пользователей и управления ими

# <a name="Запуск_проекта">Запуск проекта</a>

Клонировать репозиторий и перейти в него в командной строке:
```git
git clone https://github.com/bochikas/space.git
```
```git
cd space
```

Необходимо заполнить файл .env переменными окружения(можно взять из файла .env.example):

```
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT

SECRET_KEY
DEBUG

ALLOWED_HOSTS
```

Запустить docker-compose:
```
docker-compose up -d --build
```
Выполняем миграции:
```
docker-compose exec app python manage.py migrate --noinput
```
Создаем суперпользователя Django:
```
docker-compose exec app python manage.py createsuperuser
```
Останавливаем и удаляем контейнеры, сети, тома и образы:
```
docker-compose down -v
```

## Документация

Документация к API доступна по адресу:
```
http://127.0.0.1:8000/api/docs/
```