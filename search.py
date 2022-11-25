import easygui
from  easygui import *
import json
from logger import *

def search_base():

    title = "Поиск"

    msg = "Введите часть ФИО"
    data_input = enterbox(msg, title)
    with open("base.json", 'r', encoding='utf-8') as fh:
        base = json.load(fh)
    choices=[]
    choices.clear()
    for i in base.keys():
        if data_input in i:
            choices.append(i)
    if len(choices) == 0:
        msgbox(('Никого не удалось найти с параметром: ' + data_input))
    else:
        title = 'Найдены следующие сотрудники'
        msg = ''
        choices.append('')
        check = 1
        while check != 2:
            title = 'Список  сотрудников'
            msg = "Выберите интересующего сотрудника"
            choise = easygui.choicebox(msg, title, choices)


            if choise!=None:
                msg = (f'{choise} {base.get(choise)}')

                title = "Что вы хотите сделать?"
                button = ['Удалить', 'Вернуться к списку найденных сотрудников', 'Вернуться в меню']
                check = indexbox(msg, title, button)
                if check == 0:
                    title = "Вы уверены, что хотите удалить?"
                    button = ['Да', 'Нет']
                    yes_no = ynbox(msg, title, button)
                    if yes_no == 1:
                        base.pop(choise)
                        with open("base.json", 'w', encoding='utf-8') as fh:
                            fh.write(json.dumps(base, ensure_ascii=False))
                        easygui.msgbox(f'Я успешно удалил запись {msg}')
                        save_log(make_answer(msg, 'удаление'))
                        choices.remove(choise)



