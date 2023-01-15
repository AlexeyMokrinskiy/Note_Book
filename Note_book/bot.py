
import telebot
import base_creator
import export_in_file

token = '5802601538:AAFHIcAkL5TUyt7UJ88Xy6bBSM3AfiuBJFg'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Что будем делать? Выберите соответствующую цифру в меню:\n1. Добавить новый контакт\n2. Показать все контакты в линию\n3. Показать все контакты в колнки\n4. Экспорт\n5. Выход')


@bot.message_handler()
def do_smt(msg):
    if msg.text == '1':
        surname = bot.send_message(msg.chat.id, 'Введите Фамилию')
        bot.register_next_step_handler(surname, name_func)
    elif msg.text == '2':
        with open('line_base', 'r', encoding='utf-8') as file:
            bot.send_message(msg.chat.id, file.read())
    elif msg.text == '3':
        with open('column_base', 'r', encoding='utf-8') as file:
            bot.send_message(msg.chat.id, file.read())
    elif msg.text == '4':
        export_in_file.export_txt()
    elif msg.text == '5':
        bot.send_message(msg.chat.id, 'До свидания!')
    else:
        bot.send_message(msg.chat.id, 'Ошибка, введите цифру от 1 до 5')


def name_func(surname):
    name = bot.send_message(surname.chat.id, 'Введите Имя')
    bot.register_next_step_handler(name, phone_func, surname)


def phone_func(name, surname):
    phone = bot.send_message(name.chat.id, 'Введите номер телефона')
    bot.register_next_step_handler(phone, comment_func, surname, name)


def comment_func(phone, surname, name):
    comment = bot.send_message(phone.chat.id, 'Введите комментарий')
    bot.register_next_step_handler(comment, res_func, surname, name, phone)


def res_func(surname, name, phone, comment):
    lst = [surname.text, name.text, phone.text, comment.text]
    base_creator.column_type_base(lst)
    base_creator.line_type_base(lst)


bot.infinity_polling()


