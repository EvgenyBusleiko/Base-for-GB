import easygui
from  easygui import *
import json

from logger import *

def add_record ():
    global type_vvod
    global record
    global base

    base = {}
    record = {}
    type_vvod = ''
    output = ''
    data = []

    msg = "Введите данные сотрудника"
    title = "Добавление новой записи"
    fieldNames = ["ФИО", "Телефоны (через пробел)", "День рождения", "Месяц рождения", "Год рождения"]

    data = multenterbox(msg, title, fieldNames)
    record['телефон'] = data[1].split()
    record['дата_рождения'] = [data[2], data[3], data[4]]

    msg = "Выберите отдел"
    title = "Добавление новой записи"
    choices = ["Бухгалтерия", "Цех"]
    choise = easygui.choicebox(msg, title, choices)
    record['Отдел'] = choise
    if choise == "Бухгалтерия":
        choices = ['Кассир', "Бухгалтер"]
    else:
        choices = ['Фрезировщик', 'Сварщик', 'Токарь']
    msg = "Выберите должность"
    choise2 = easygui.choicebox(msg, title, choices)
    record['Должность'] = choise2
    msg = (f'{data[0]} {record}')
    title = "Вы хотите добавить?"
    button = ['Да', 'Нет']
    yes_no = ynbox(msg, title, button)

    if yes_no == 1:
        with open("base.json", 'r', encoding='utf-8') as fh:
            base = json.load(fh)

        base.update({data[0]: record})

        with open("base.json", 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(base, ensure_ascii=False))

            easygui.msgbox('Я успешно загрузил в файл информацию')
            save_log(make_answer((f'{data[0]} {base.get(data[0])}'), 'запись'))

# add_record()