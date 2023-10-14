## Сервис Building
### О Проекте:
#### *Building - это сервис, который принимает запросы с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер и выдаёт результат запроса.*
### Возможности проекта:
* #### Сохранение запроса на сервер и ответ с внешнего сервера в БД
* #### API который выводит историю всех запросов/историю по кадастровому номеру
### Ключевые эндпоинты:
1. #### `/query`  - получение запроса от пользователя и отправка результата пользователю
2. #### `/ping` - проверка работы сервера
3. #### `/history` - это эндпоинт API с историей всех запросов/по кадастровому номеру
4. #### `http://127.0.0.1:5000/admin/` - по адресу находится админ-панель 
### Используемый стек технологий:
* #### Python 3.11
* #### Flask 3.0.0
* #### SQLAlchemy 2.0.21
* #### Alembic 1.11.1
* #### Flask-Admin 1.6.1
* #### Flask-WTF 1.2.1
* #### flask-bootstrap 3.3.7.1
### Инструкции по развёртыванию проекта:
* #### *Клонировать репозиторий и перейти в него в командной строке:*
```
git@github.com:SkaDin/real_estate_service.git

cd real_estate_service
```
* #### *Установите зависимости и активируйте виртуальное окружение:*
```commandline
poetry install
poetry shell
poetry update
```
* #### *Пример .env-файла который должен быть создан в корне проекта:*
```
FLASK_APP=app
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=My_favorite_micro-framework_is_FLASK!
BASIC_AUTH_USERNAME=Admin
BASIC_AUTH_PASSWORD=Admin007
```
* #### *Для получения отчёта о покрытии приложения тестами можно воспользоваться командой:*
```commandline
coverage run -m pytest
coverage report
```
* #### *Сами тесты запускаются командой:*
```commandline
python -m pytest -W ignore
```
* #### *Добавить несколько тестовых записей в базу данных:*
```commandline
flask load_data
```
* #### *Запуск приложения:*
```commandline
flask run
```
* #### *Добавлен Dockerfile и работа с образом:*
1. Перейти в корень приложения(Где лежит Dockerfile)
2. Создать образ приложения:
```commandline
sudo docker build -t real_estate_service . 
```
3. Затем, когда образ соберёт контейнер, запустить его:
```commandline
sudo docker run -p 5000:5000 -p 8000:8000 real_estate_service
```
4. Не забыть удалить образы и контейнеры которые не нужны:
```commandline
sudo docker container rm -f ID_CONTAINER
sudo docker image rm -f ID_IMAGE
```
* #### *Автор: SkaDin(Денис Сушков)*

