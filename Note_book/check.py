def digit_check():
    try:
        input_number = int(input('Введите число от 1 до 5: \n'))
        if 0 < input_number < 6:
            return input_number
        else:
            return digit_check()
    except ValueError:
        print('Это должно быть число\n')
        return digit_check()