# POLY-VISITORS

Курсовой проект Python + Django

## Команды запуска

1. Старт проекта `python manage.py runserver`
2. Старт линтера `flake8 ./`
3. Создать миграции `python manage.py makemigrations`
4. Применить миграции `python manage.py migrate`

## URL запуска

1. Админ панель `/admin`
2. Swagger `/swagger`
3. Redoc `/redoc`

## Команды для фикстур

### Для получения фикстур
1. Заявления <br/>
    `python manage.py dumpdata main.Statement --format=json --indent=4 -o main/fixtures/statements.json`
2. Общежития <br/>
    `python manage.py dumpdata main.Dormitory --format=json --indent=4 -o main/fixtures/dormitories.json`
3. Студенты <br/>
    `python manage.py dumpdata users.Students --format=json --indent=4 -o users/fixtures/students.json`
4. Коменданты <br/>
    `python manage.py dumpdata users.Commandants --format=json --indent=4 -o users/fixtures/commandants.json`

### Для применения фикстур (Нужен формат UTF-8)
1. Заявления <br/>
    `python manage.py loaddata main/fixtures/statements.json`
2. Общежития <br/>
    `python manage.py loaddata main/fixtures/dormitories.json`
3. Студенты <br/>
    `python manage.py loaddata users/fixtures/students.json`
4. Коменданты <br/>
    `python manage.py loaddata users/fixtures/commandants.json`

## Команды для PyLint
Оценка кода: 10.00/10

1. Запуск проверки <br/>
    `pylint ./`