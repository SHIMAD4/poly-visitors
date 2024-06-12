# POLY-VISITORS

Курсовой проект Python + Django

## Команды запуска
Оценка кода по линтеру: 10.00/10

1. Старт проекта `python manage.py runserver`
2. Старт линтера `pylint ./`
3. Создать миграции `python manage.py makemigrations`
4. Применить миграции `python manage.py migrate`
5. Docker `docker-compose up`

## URL запуска

1. Админ панель `/admin`
2. Swagger `/swagger`
3. Redoc `/redoc`

## Команды для фикстур

### Для получения фикстур
1. Заявления <br/>
    `docker-compose exec web python manage.py dumpdata main.Statements --format=json --indent=4 -o main/fixtures/statements.json`
2. Общежития <br/>
    `docker-compose exec web python manage.py dumpdata main.Dormitory --format=json --indent=4 -o main/fixtures/dormitories.json`
3. Студенты <br/>
    `docker-compose exec web python manage.py dumpdata users.Students --format=json --indent=4 -o users/fixtures/students.json`
4. Коменданты <br/>
    `docker-compose exec web python manage.py dumpdata users.Commandants --format=json --indent=4 -o users/fixtures/commandants.json`
5. Группы <br/>
    `docker-compose exec web python manage.py dumpdata auth.Group --format=json --indent=4 -o users/fixtures/auth_groups.json`

### Для применения фикстур (Нужен формат UTF-8)
1. Заявления <br/>
    `docker-compose exec web python manage.py loaddata main/fixtures/statements.json`
2. Общежития <br/>
    `docker-compose exec web python manage.py loaddata main/fixtures/dormitories.json`
3. Студенты <br/>
    `docker-compose exec web python manage.py loaddata users/fixtures/students.json`
4. Коменданты <br/>
    `docker-compose exec web python manage.py loaddata users/fixtures/commandants.json`
5. Группы <br/>
    `docker-compose exec web python manage.py loaddata users/fixtures/auth_groups.json`