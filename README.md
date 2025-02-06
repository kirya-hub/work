# Lyceum project

## Установка:

```bash
cd ~/lessons/lyceum
python3 -m venv venv
source venv/bin/activate
```


## Зависимости среды:

#### Production:
pip install -r requirements/prod.txt

#### Development:
pip install -r requirements/dev.txt

#### Testing:
pip install -r requirements/test.txt


## Запуск сервера:
python manage.py runserver


## Настройка переменных окружения:

**Создать файл .env в корне проекта:**
touch .env

**Заполнить его своими данными:**
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=example.com,localhost,127.0.0.1


## Запуск в dev-режиме:

```bash
pip install -r requirements/dev.txt
python manage.py runserver
```