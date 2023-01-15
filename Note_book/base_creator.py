import os
os.chdir(os.path.dirname(__file__))
import control


def line_type_base(data):   
    surname, name, telephon, commit = data
    with open('line_base', 'a', encoding='UTF-8') as file:
        file.write('{} {}; тел - {}, комментарий - {}:\n'.format(surname, name, telephon, commit))

def column_type_base(data):   
    surname, name, telephon, commit = data
    with open('column_base', 'a', encoding='UTF-8') as file:
        file.write('{}\n{}\n{}\n{}\n\n'.format(surname, name, telephon, commit))
    print('Контакт успешно добавлен')
    control.choise()