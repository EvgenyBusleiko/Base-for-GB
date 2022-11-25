# Base-for-GB
Рад представить вашему вниманию простейшую базу данных.

*Что умеет данная программа?*
* Сохранять данные пользователя - ФИО, телефоны, дату рождения, отдел и должность
* Осуществляет поиск по части ФИО
* Позволяет удалить ненужных сотрудников
* Все действия по удалению и добавлению  сохраняются в log файл

# *Структура программы*

Основным файлом является user_interface.py
Файл record_new.py - добавление новых сотрудников
Файл search.py - поиск по базе
Файл change.py - удаление записи
Файл logger.py - сохранение логов
Файлы base.json и log.txt хранят соответственно базу и логи

# *Описание работы программы*

При запуске программы мы попадаем в главное меню:

![Вид меню](https://github.com/EvgenyBusleiko/Base-for-GB/blob/main/main_menu.jpg)

Тут можно просмотреть базу/добавить новых сотрудников/ осуществить поиск
По завершении любого действия мы вернемся в это меню:

*Просмотр базы*

Нажав этот пункт мы увидим список ФИО всех сотрудников

![Список всех сотрудников](https://github.com/EvgenyBusleiko/Base-for-GB/blob/main/all_record_window.jpg)


Выбрав запись мы увидим подробную информацию о ней и варианты действий


![Один сотрудник](https://github.com/EvgenyBusleiko/Base-for-GB/blob/main/one_record_window.jpg)

*Добавить новую запись*

Выбрав этот пункт, мы попадем в такое меню


![Новая запись](https://github.com/EvgenyBusleiko/Base-for-GB/blob/main/input_data.jpg)

Далее предложат выбрать отдел из имеющихся

![Отдел](https://github.com/EvgenyBusleiko/Base-for-GB/blob/main/departmet_choice.jpg)



И профессию, так же из имеющихся


![Профессия](https://github.com/EvgenyBusleiko/Base-for-GB/blob/main/profession_choice.jpg)


*Поиск по базе*

Появляется окно, куда можно ввести часть имени или фамилии

![Профессия](https://github.com/EvgenyBusleiko/Base-for-GB/blob/main/search_window.jpg)

Далее окно с найденными результатами:

![Один сотрудник](https://github.com/EvgenyBusleiko/Base-for-GB/blob/main/all_record_window.jpg)

Выбрав конкретного сотрудника можно просмотреть информацию о нем и выбрать варианты действий:

![Один сотрудник](https://github.com/EvgenyBusleiko/Base-for-GB/blob/main/one_record_window.jpg)

Если выбрать "Удалить", программа запросит подтверждение действия

![Один сотрудник](https://github.com/EvgenyBusleiko/Base-for-GB/blob/main/approvement.jpg)

После этого будет показано служебное сообщение, запись будет удалена из базы и программа вернется к списку найденных сотрудников:

![Один сотрудник](https://github.com/EvgenyBusleiko/Base-for-GB/blob/main/service_window.jpg)

Спасибо за внимание!


