
import control
path_to_db = 'line_base'


def export_txt():

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for i in range(0, len(data)):
                with open('Export_contact.csv', 'a', encoding='UTF-8') as export:
                    export.write('\n' + "".join(data[i]))

    print('\nКонтакты успешно экспортированы в файл!\n')
    control.choise()