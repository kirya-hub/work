# Lyceum project

## Установка:

```bash
cd ~/lessons/lyceum
python3 -m venv venv
source venv/bin/activate
```


## Зависимости среды:

#### Production:

```bash
pip install -r requirements/prod.txt
```

#### Development:

```bash
pip install -r requirements/dev.txt
```

#### Testing:

```bash
pip install -r requirements/test.txt
```

## Запуск сервера:

```bash
python manage.py runserver
```


## Настройка переменных окружения:

**Создать файл .env в корне проекта:**

```bash
touch .env
```


**Заполнить его своими данными:**

```bash
DJANGO_SECRET_KEY=your-secret-key

DJANGO_DEBUG=True

DATABASE_URL=sqlite:///db.sqlite3

DJANGO_ALLOWED_HOSTS=example.com,localhost,127.0.0.1
```


## Запуск в dev-режиме:

```bash
pip install -r requirements/dev.txt
python manage.py runserver
```