# Тестовое задание

### Установка
Клонируйте репозиторий себе

`git clone https://github.com/akariasmorum/test_task.git`

Перейдите в test_task:

`cd test_task`

Запуск Django:

`python manage.py runserver`

В браузере переходим по ссылке:
`http://localhost:8000/get-process`

### Фильтры
Накладываются в виде GET-параметров в адресной строке браузера

##### proc_range 
выводит процессы в указанном диапазоне

`http://localhost:8000/get-process?proc_range=100-1000` Вернет процессы, PID которых находится в диапозоне 100-1000

##### cmd_start

Выводит процессы, COMMAND которых начинается с указанного набора символов:
`http://localhost:8000/get-process?cmd_start=/usr` Вернет процессы, COMMAND которых начинается с /usr

##### cmd_reg

Выводит процессы COMMAND Которых соответсвует указанному регулярному выражению:
`http://localhost:8000/get-process?cmd_reg=\d{2} Вернет процессы, в которых в COMMAND содержится >= двух цифр

