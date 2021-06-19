# Цифровой прорыв 2021

Тема: Разработка системы дистанционного мониторинга уровня артериального давления и пульса у больных с артериальной гипертензией

Команда: Острые предметы

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Sharp-Objects_dashboard&metric=alert_status)](https://sonarcloud.io/dashboard?id=Sharp-Objects_dashboard)
[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/dashboard?id=Sharp-Objects_dashboard)

## Описание

Личный кабинет пациента и врача

## Использование

```bash
$ # Клонирование кода
$ git clone https://github.com/Sharp-Objects/dashboard.git
$ cd dashboard
$
$ # Настройка виртуального окружения (Unix)
$ virtualenv env
$ source env/bin/activate
$
$ # Настройка виртуального окружения (Windows)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Установка модулей - SQLite Database
$ pip3 install -r requirements.txt
$
$ # Альтернативная установка модулей - PostgreSQL connector
$ # pip install -r requirements-pgsql.txt
$
$ # Создание переменной окружения FLASK_APP 
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Запуск режима разработчика 
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Запуск приложения (режим разработчика)
$ # --host=0.0.0.0 - публикация на все сетевые интерфейсы (default 127.0.0.1)
$ # --port=5000    - выбор порта (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Доступ в браузере: http://127.0.0.1:5000/
```
