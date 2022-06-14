# Учебный проект по курсу Python-разработчик

Web-приложение для отслеживания погоды и ведения блога.

## Использованные технологии:

- GIT
- python
- django
- django-crispy-forms
- requests

## Инструкция по запуску приложения

1. Клонируем репозиторий (или определенную ветку) и заходим в папку:
```
>>> git clone --branch master https://github.com/Lisanis/Site_project.git
>>> cd site_project/sitegroup139
```
2. Генерируем Django Secret Key и добавляем в файл /creds/key.py (SECRET_KEY = 'Django Secret Key'):
```
>>> from django.core.management import utils
>>> print(utils.get_random_secret_key())
```
3. Регистрируемся в https://openweathermap.org и в личном кабинете генерируем свой Weather API Key, который также добавляем в файл /creds/key.py (MY_API_KEY = 'Weather API Key')

4. Устанавливаем пакеты из requirements.txt:
```
>>> pip install -r requirements.txt
```
5. Запускаем миграции для работы с базой данных:
```
>>> manage.py migrate
```
6. Запускаем сервер:
```
>>> python manage.py runserver
```
7. Приложение доступно по адресу http://127.0.0.1:8000/
8. Для работы в Django-admin создаем суперпользователя:
```
>>> python manage.py createsuperuser
```
