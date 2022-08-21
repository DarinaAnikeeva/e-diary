# Электронный дневник школы

Этот сайт - интерфейс для учеников школы. Здесь можно посмотреть оценки, расписание и прочую открытую информацию. Учителя заполняют базу данных через другой сайт. Ставят там оценки и т.д.

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте БД командой `python3 manage.py migrate`
- Скопируйте в папку с файлом manage.py базу данных с оценками учеников schoolbase.sqlite3
- Запустите сервер командой python3 manage.py runserver Вы увидите:

```
System check identified no issues (0 silenced).
August 20, 2022 - 12:29:09
Django version 2.2.24, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Сайт будет доступен по адресу http://127.0.0.1:8000/ Чтобы остановить работу сервера нажмите Crtrl C

## Внесение изменений в дневник

Для начала запустите: `python manage.py shell`. Далее ввести в открывшееся поле:
```
import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid, Lesson, Mark, Chastisement, Commendation
from script import fix_marks, remove_chastisements, create_commendation
```

### Изменение данных

 - `fix_marks('Имя и фамилия')` - функция меняет все двойки и тройки на пятёрки.
Пример запуска: `fix_marks('Фролов Иван')`

 - `remove_chastisements('Имя и фамилия')` - удаляет все имеющиеся замечания.
Пример запуска: `remove_chastisements('Фролов Иван')`

 - `create_commendation('Имя и фамилия', 'Предмет')` - создает похвалу по последнему уроку введенного предмета.            
 Пример запуска: `create_commendation('Фролов Иван', 'Математика')`
 
 Для просмотра изменений выходим из shell командой `quit` и запускаем сервер командой `python3 manage.py runserver`


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
