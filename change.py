import easygui
from  easygui import *
import json
from logger import *



def change_record():
    global file
    file=[]
    choices=[]
    with open("base.json", 'r', encoding='utf-8') as fh:
        base = json.load(fh)
    choices.clear()

    for i in base.keys():
        choices.append(i)
    check=1
    while check!=2:
        title = 'Список  сотрудников'
        msg = "Выберите интересующего сотрудника"
        choise = easygui.choicebox(msg, title, choices)
        if choise != None:
            msg = (f'{choise} {base.get(choise)}')

            title = "Что вы хотите сделать?"
            button = ['Удалить', 'Вернуться к списку сотрудников', 'Вернуться в меню']
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


# change_record()