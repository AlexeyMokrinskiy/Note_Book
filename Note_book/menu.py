import check

def user_choise():
    what_to_do = 'Что будем делать? Выберите соответствующую цифру в меню:'
    new_contact = '1. Добавить новый контакт'
    view_line_contact = '2. Показать все контакты в линию'
    view_column_contact = '3. Показать все контакты в колнки'
    export_to_file = '4. Экспорт'
    to_exit = '5. Выход'

    print(f'{what_to_do}\n\n{new_contact}\n{view_line_contact}\n{view_column_contact}\n{export_to_file}\n{to_exit}')
    return check.digit_check()
