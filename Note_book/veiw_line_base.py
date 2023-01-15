import control
path = 'line_base'

def view_lb():
    with open(path, 'r', encoding='UTF-8') as file:
        s = file.readlines()
        for i in range(0, len(s)):
            print(s[i])
    control.choise()
