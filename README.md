# Mail notifications

### Что ты такое?

Сервис по доставке уведомлений (напоминалок) по почте.

### Стек

Python, Django, Celery, Redis, Docker.

### Как запустить?

Склонируйте репозиторий:

```bash
git clone https://github.com/sh4rpy/mail_notifications.git
```

Создайте файл .env в одной директории с файлом settings.py. Создайте в нем переменную окружения  SECRET_KEY, которой присвойте скопированный ключ с [сайта генерации ключей](https://djecrety.ir). Далее добавьте переменные для работы с SMTP Яндекса. Выглядеть файл должен так:

```python
SECRET_KEY=скопированный_ключ
EMAIL_HOST_USER=ваша_почта
EMAIL_HOST_PASSWORD=ваш_пароль
```

Запустите **docker-compose** командной:

```bash
docker-compose up
```

Сервис станет доступен по адресу [http://0.0.0.0:8000](http://0.0.0.0:8000). Создайте суперпользователя внутри контейнера web:

```bash
docker exec -it <container_id> python manage.py createsuperuser
```

Перейдите на страницу сервиса и авторизуйтесь в админ-панели. Готово!