import easygui
from easygui import *
import json
from record_new import add_record as add_r
from change import *
from  search import *

def menu():
    global type_vvod
    global record
    global base
    global file
    file=[]
    base={}
    record={}
    type_vvod = ''
    output=''
    while output != "Выход":
        msg = "Выберите пункт меню"
        title = "Меню"
        choices = ["Просмотр базы/удаление", "Добавить новую запись", \
        "Поиск по базе", "Выход"]
        output = easygui.choicebox (msg, title, choices)

        if output == "Просмотр базы/удаление":
            change_record()

        elif output == "Добавить новую запись":
            add_r()

        elif output == "Поиск по базе":
            search_base()

        elif output == "Выход":
            exit()

menu()
