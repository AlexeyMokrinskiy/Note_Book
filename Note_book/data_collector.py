def get_value():
    return input('->:')


def input_data():
    print('\nВведите Фамилию')
    surname = get_value()
    print('\nВведите Имя')
    name = get_value()
    print('\nВведите Телефон')
    telephon = get_value()
    print('\nВведите Комментарий')
    commit = get_value()
    return (surname, name, telephon, commit)

# print(input_data())