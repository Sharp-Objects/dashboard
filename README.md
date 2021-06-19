[![We recommend IntelliJ IDEA](https://www.elegantobjects.org/intellij-idea.svg)](https://www.jetbrains.com/idea/)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Sharp-Objects_dashboard&metric=bugs)](https://sonarcloud.io/dashboard?id=Sharp-Objects_dashboard)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Sharp-Objects_dashboard&metric=code_smells)](https://sonarcloud.io/dashboard?id=Sharp-Objects_dashboard)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Sharp-Objects_dashboard&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=Sharp-Objects_dashboard)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Sharp-Objects_dashboard&metric=ncloc)](https://sonarcloud.io/dashboard?id=Sharp-Objects_dashboard)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Sharp-Objects_dashboard&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=Sharp-Objects_dashboard)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Sharp-Objects_dashboard&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=Sharp-Objects_dashboard)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Sharp-Objects_dashboard&metric=security_rating)](https://sonarcloud.io/dashboard?id=Sharp-Objects_dashboard)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Sharp-Objects_dashboard&metric=sqale_index)](https://sonarcloud.io/dashboard?id=Sharp-Objects_dashboard)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Sharp-Objects_dashboard&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=Sharp-Objects_dashboard)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Описание

Личный кабинет пациента и врача, созданный с целью дистанционного мониторинга уровня артериального давления и пульса.
Данная система позволяет сохранять текущие результаты измеряемых значений с помощью ручного ввода или голосового
управления. Информация пациента сохраняется в базе данных и передаётся врачу. На её основе доктор делает медицинские
рекомендации.

<br/>

> Реализованная функциональность:

- REST сервис;
- Личный кабинет врача;
- Личный кабинет пациента;
- Мобильное приложение

<br/>

> Особенность проекта:

- Голосовой ввод данных;
- Простота интеграции;
- Получение и отправка данных в разные источники;
- Рекомендательная система лекарств от врача;
- Рекомендательная система действий в приложении

<br/>

> Стек технологий

- DBMS: SQLite, PostgreSQL (production)
- DB Tools: SQLAlchemy ORM, Flask-Migrate (schema migrations)
- Modular design with **Blueprints**, simple codebase
- Session-Based authentication (via **flask_login**), Forms validation
- Deployment scripts: Docker, Gunicorn / Nginx, Heroku
- Python with Flask

> Примечание: чтобы использовать приложение, перейдите на страницу регистрации и создайте нового пользователя. После аутентификации приложение разблокирует приватные страницы.

### Демо

Демоверсия приложения расположена на AWS по адресу: http://ec2-3-15-18-180.us-east-2.compute.amazonaws.com:5000

Реквизиты тестовых пользователей:

1. Пациент

- логин: test
- пароль: test

2. Доктор

- логин: doctor
- пароль: doctor

## Использование

```bash
# Клонирование кода
git clone https://github.com/Sharp-Objects/dashboard.git
cd dashboard

# Настройка виртуального окружения (Unix)
virtualenv env
source env/bin/activate

# Настройка виртуального окружения (Windows)
# virtualenv env
# .\env\Scripts\activate

# Установка модулей - SQLite Database
pip3 install -r requirements.txt

# Альтернативная установка модулей - PostgreSQL connector
# pip install -r requirements-pgsql.txt

# Создание переменной окружения FLASK_APP 
(Unix/Mac) export FLASK_APP=run.py
(Windows) set FLASK_APP=run.py
(Powershell) $env:FLASK_APP = ".\run.py"

# Запуск режима разработчика 
# (Unix/Mac) export FLASK_ENV=development
# (Windows) set FLASK_ENV=development
# (Powershell) $env:FLASK_ENV = "development"

# Запуск приложения (режим разработчика)
# --host=0.0.0.0 - публикация на все сетевые интерфейсы (default 127.0.0.1)
# --port=5000    - выбор порта (default 5000)  
flask run --host=0.0.0.0 --port=5000

# Доступ в браузере: http://127.0.0.1:5000/
```

## Развёртывание

Приложение имеет базовую конфигурацию, которая будет выполняться в [Docker](https://www.docker.com/)
и [Gunicorn](https://gunicorn.org/).

<br/>

### [Docker](https://www.docker.com/)
---

Приложение легко запускается в docker-контейнере. Шаги:

> Клонирование кода

```bash
git clone https://github.com/Sharp-Objects/dashboard.git
cd dashboard
```

> Запуск приложения

```bash
sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Перейдите в браузере на страницу `http://localhost:5005`. Приложение развернуто и готово к запуску.

<br/>

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' - это HTTP-сервер Python WSGI для UNIX.

> Установка gunicorn

```bash
pip install gunicorn
```

> Запустите приложение, используя gunicorn

```bash
gunicorn --bind 0.0.0.0:8001 run:app
Serving on http://localhost:8001
```

Перейдите в браузере на страницу `http://localhost:8001`. Приложение развернуто и готово к запуску.

