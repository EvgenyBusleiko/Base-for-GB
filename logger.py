import datetime
import easygui



def make_answer (key,operation):
    answer=''
    current_date_time =str( datetime.datetime.now())
    answer=current_date_time+' '+operation+' '+key+'\n'
    return answer

def save_log(answer_in_string):
    with open("log.txt", 'a', encoding='utf-8') as fh:

        fh.write(answer_in_string)

        # easygui.msgbox(answer_in_string,'Я успешно загрузил в log файл информацию')