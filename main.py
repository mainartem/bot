import telebot
import time
from telebot import types
import re

unt = 0

bot = telebot.TeleBot("5996201646:AAGLoW74ThJiWDTR08AVLul0QJYvnMUd8UU")

scores = {2145329973: 10}  # id: ball


@bot.message_handler(commands=['login'])
def login(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, 'Для того чтобы войти отправти свой номер телефона ', reply_markup=keyboard)


# @bot.message_handler(commands=['start'])
# def start(message):
#     # mess=f"Добрый день, {message.from_user.first_name} {message.from_user.last_name}. Мы рады приветствовать Вас на курсе по програмирование PYTHON CODE. Хотелось познакомить Вас с командами нашего бота "+"\n"+"Войти в учетную запись 🚪 - /login""\n"+"Зарегистрироватся для оплаты 💳 - /reg""\n"+" Главное меню 📱 - /menu"
#     # bot.send_message(message.chat.id, mess)
#     # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     # Tem1 = types.KeyboardButton('Введение')
#     # markup.add(Tem1)
#     # bot.send_message(message.chat.id, "Добрый день. Для того, чтобы пройти тестирование выберити одну из тем.   ", reply_markup=markup)
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True)
#     keyboard.add(button_phone)
#     bot.send_message(message.chat.id, 'Для того чтобы войти отправти свой номер телефона ', reply_markup=keyboard)
#     print(message.from_user.id)


@bot.message_handler(commands=['start'])
def start(message):
    print(message.from_user.id)

    if message.from_user.id in phone.keys():
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        button1 = types.KeyboardButton('📚 Курс 📚')
        button2 = types.KeyboardButton('📝 Тесты 📝')
        button3 = types.KeyboardButton('🖊 Практические задания 🖊')
        menu.add(button1, button2, button3)
        bot.send_message(message.chat.id, "Вы попали в главное меню. (%i)" % scores[message.from_user.id], reply_markup=menu)
    else:
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,
                         "Данный номер телефона не зарегистрирован за консультацией введите команду /reg",
                         reply_markup=keyboard)

# @bot.message_handler(commands=['menu'])
# def menu(message):
#   global unt
#   if unt == 0:
#       bot.send_message(message.chat.id, "<b>🔒 Для на начала войдите в учетную запись для разблокировки курса🔒</b>", parse_mode="html")
#   if unt == 1:
#       menu= types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#       button1 = types.KeyboardButton('📚 Курс 📚')
#       button2 = types.KeyboardButton('📝 Тесты 📝')
#       button3 = types.KeyboardButton('🖊 Практические задания 🖊')
#       menu.add(button1, button2, button3)
#       bot.send_message(message.chat.id, "Вы попали в главное меню.", reply_markup=menu)

@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        print(type(message.contact))
        print('Name: ' + str(message.contact.first_name))
        print('Phone: ' + str(message.contact.phone_number))

        # phone_number = re.sub("[^0-9]", "", message.contact.phone_number)

        if message.from_user.id in phone.keys():
            # unt = 1
            # keyboard = types.ReplyKeyboardRemove()
            # bot.send_message(message.chat.id, "Вы успешно авторизовались на нашем сервисе!!! Теперь Вы можете использовать материаллы нашего курса, для этого введите команду /menu ", reply_markup=keyboard)
            menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            button1 = types.KeyboardButton('📚 Курс 📚')
            button2 = types.KeyboardButton('📝 Тесты 📝')
            button3 = types.KeyboardButton('🖊 Практические задания 🖊')
            menu.add(button1, button2, button3)
            bot.send_message(message.chat.id, "Вы попали в главное меню.", reply_markup=menu)


        else:
            keyboard = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id,
                             "Данный номер телефона не зарегистрирован за консультацией введите команду /reg",
                             reply_markup=keyboard)


@bot.message_handler()
def get_user_text(message):
    if message.text == "📚 Курс 📚":
        Kurs = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        K1 = types.KeyboardButton('Введение')
        Kurs.add(K1)
        bot.send_message(message.chat.id, "Выберите одну из тем нашего курса для его изучения.", reply_markup=Kurs)
    if message.text == "📝 Тесты 📝":
        test = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        t1 = types.KeyboardButton('Тестовое задание №1 (Введение)')
        test.add(t1)
        bot.send_message(message.chat.id, "Выберите одну из тестовых заданий для его прохождения.", reply_markup=test)
    if message.text == "🖊 Практические задания 🖊":
        bot.send_message(message.chat.id, "Практических заданий на данный момент нет")

    # Курс
    if message.text == "Введение":
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,
                         "<b>§1 Введение</b>" + "\n" + "<b><i>Что такое Python?</i></b>" + "\n" + "Python - это высокоуровневый язык программирования, который был разработан в конце 1980-х годов. Он отличается простым и понятным синтаксисом, что делает его очень доступным для новичков. Одной из главных особенностей Python является его способность работать на многих платформах, включая Windows, MacOS и Linux, что делает его одним из наиболее гибких языков программирования. В целом, Python - это мощный язык программирования, который может быть использован как для начинающих, так и для опытных программистов. Python является интерпретируемым языком программирования, в котором код выполняется непосредственно интерпретатором, без предварительной компиляции. Код на интерпретируемом языке может быть исполнен построчно, что делает процесс разработки более удобным и быстрым. Однако, исполнение кода на интерпретируемом языке может быть медленнее по сравнению с компилируемыми языками. Кроме того, Python также имеет множество инструментов, которые помогают в разработке и тестировании программ, таких как PyCharm, Jupyter Notebook, Pytest и многие другие. В целом, Python является одним из самых популярных языков программирования в мире, и его популярность продолжает расти с каждым годом. Если вы хотите научиться программированию, Python - это отличный выбор. " + "\n" + "<b><i>Где применяется язык программирования Python?</i></b>" + "\n" + "Python является очень популярным и многофункциональным языком программирования, который применяется во многих сферах. Вот некоторые из них" + "\n" + "• Веб-разработка: Python используется для создания веб-приложений и сайтов. Некоторые из самых популярных веб-фреймворков, например, Django и Flask, написаны на Python." + "\n" + "• Наука о данных: Python является одним из самых популярных языков для анализа данных и машинного обучения. Библиотеки, такие как NumPy, Pandas и SciPy, делают Python идеальным инструментом для работы с данными." + "\n" + "• Искусственный интеллект: Python широко используется в разработке искусственного интеллекта и машинного обучения. Библиотеки, такие как TensorFlow и PyTorch, делают Python одним из наиболее популярных языков для разработки нейронных сетей." + "",
                         reply_markup=keyboard, parse_mode="html")

    if message.text == "Тестовое задание №1 (Введение)":
        ball = 0
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        vop1 = types.KeyboardButton("Высокоуровневый язык программирования ")
        vop2 = types.KeyboardButton('Стандартизированный язык гипертекстовой разметки')
        vop3 = types.KeyboardButton('Текстовый процессор, предназначенный для создания, просмотра')
        markup2.add(vop1, vop2, vop3)
        bot.send_message(message.chat.id, "Что такое PYTHON", reply_markup=markup2)

    if message.text == "Высокоуровневый язык программирования":
        ball = ball + 10
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v2op1 = types.KeyboardButton("Компилируемый ")
        v2op2 = types.KeyboardButton('Интепритируемый')
        v2op3 = types.KeyboardButton('Не интепритируемый и не компилируемый')
        markup3.add(v2op1, v2op2, v2op3)
        bot.send_message(message.chat.id, "Язык програмирование PYTHON является", reply_markup=markup3)

    if message.text == "Стандартизированный язык гипертекстовой разметки":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v2op1 = types.KeyboardButton("Компилируемый ")
        v2op2 = types.KeyboardButton('Интепритируемый')
        v2op3 = types.KeyboardButton('Не интепритируемый и не компилируемый')
        markup3.add(v2op1, v2op2, v2op3)
        bot.send_message(message.chat.id, "Язык програмирование PYTHON является", reply_markup=markup3)
    if message.text == "Текстовый процессор, предназначенный для создания, просмотра":
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v2op1 = types.KeyboardButton("Компилируемый ")
        v2op2 = types.KeyboardButton('Интепритируемый')
        v2op3 = types.KeyboardButton('Не интепритируемый и не компилируемый')
        markup3.add(v2op1, v2op2, v2op3)
        bot.send_message(message.chat.id, "Язык програмирование PYTHON является", reply_markup=markup3)

    if message.text == "Интепритируемый":
        ball = ball + 10
        markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v3op1 = types.KeyboardButton("Можно работать с базами данных")
        v3op2 = types.KeyboardButton('Нельзя работать с базами данных')
        v3op3 = types.KeyboardButton('Можно работать только с малыми базами')
        markup4.add(v3op1, v3op2, v3op3)
        bot.send_message(message.chat.id, "Можно ли на языке програмирование PYTHON работать с большими базами данных",
                         reply_markup=markup4)
    if message.text == "Компилируемый":
        markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v3op1 = types.KeyboardButton("Можно работать с базами данных")
        v3op2 = types.KeyboardButton('Нельзя работать с базами данных')
        v3op3 = types.KeyboardButton('Можно работать только с малыми базами')
        markup4.add(v3op1, v3op2, v3op3)
        bot.send_message(message.chat.id, "Можно ли на языке програмирование PYTHON работать с большими базами данных",
                         reply_markup=markup4)
    if message.text == "Не интепритируемый и не компилируемый":
        markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v3op1 = types.KeyboardButton("Можно работать с базами данных")
        v3op2 = types.KeyboardButton('Нельзя работать с базами данных')
        v3op3 = types.KeyboardButton('Можно работать только с малыми базами')
        markup4.add(v3op1, v3op2, v3op3)
        bot.send_message(message.chat.id, "Можно ли на языке програмирование PYTHON работать с большими базами данных",
                         reply_markup=markup4)
    if message.text == "Можно работать с базами данных":
        ball = ball + 10

        markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v4op1 = types.KeyboardButton("Tим Петерс")
        v4op2 = types.KeyboardButton('Гвидо ван Россум')
        v4op3 = types.KeyboardButton('Ларри Пейдж')
        markup5.add(v4op1, v4op2, v4op3)
        bot.send_message(message.chat.id, "Кто создал Дзен Питона", reply_markup=markup5)
    if message.text == "Нельзя работать с базами данных":
        markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v4op1 = types.KeyboardButton("Tим Петерс")
        v4op2 = types.KeyboardButton('Гвидо ван Россум')
        v4op3 = types.KeyboardButton('Ларри Пейдж')
        markup5.add(v4op1, v4op2, v4op3)
        bot.send_message(message.chat.id, "Кто создал Дзен Питона", reply_markup=markup5)
    if message.text == "Можно работать только с малыми базами":
        markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v4op1 = types.KeyboardButton("Tим Петерс")
        v4op2 = types.KeyboardButton('Гвидо ван Россум')
        v4op3 = types.KeyboardButton('Ларри Пейдж')
        markup5.add(v4op1, v4op2, v4op3)
        bot.send_message(message.chat.id, "Кто создал Дзен Питона", reply_markup=markup5)
    if message.text == "Tим Петерс":
        ball = ball + 10
        markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v5op1 = types.KeyboardButton("python-xy.github.io")
        v5op2 = types.KeyboardButton('github.com›python')
        v5op3 = types.KeyboardButton('python.org')
        markup6.add(v5op1, v5op2, v5op3)
        bot.send_message(message.chat.id, "Выберите офицальный сайт PYTHON", reply_markup=markup6)
    if message.text == "Гвидо ван Россум":
        markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v5op1 = types.KeyboardButton("python-xy.github.io")
        v5op2 = types.KeyboardButton('github.com›python')
        v5op3 = types.KeyboardButton('python.org')
        markup6.add(v5op1, v5op2, v5op3)
        bot.send_message(message.chat.id, "Выберите офицальный сайт PYTHON", reply_markup=markup6)
    if message.text == "Ларри Пейдж":
        markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v5op1 = types.KeyboardButton("python-xy.github.io")
        v5op2 = types.KeyboardButton('github.com›python')
        v5op3 = types.KeyboardButton('python.org')
        markup6.add(v5op1, v5op2, v5op3)
        bot.send_message(message.chat.id, "Выберите офицальный сайт PYTHON", reply_markup=markup6)
    if message.text == "python.org":
        ball = ball + 10
        markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v6op1 = types.KeyboardButton("Использовать IDE или IDLE")
        v6op2 = types.KeyboardButton('Использовать Word')
        v6op3 = types.KeyboardButton('Использовать IDE или IDLE, так же можно писать в CMD и в блокноте')
        markup7.add(v6op1, v6op2, v6op3)
        bot.send_message(message.chat.id, "Как можно писать программы на языке PYTHON", reply_markup=markup7)

    if message.text == "github.com›python":
        markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v6op1 = types.KeyboardButton("Использовать IDE или IDLE")
        v6op2 = types.KeyboardButton('Использовать Word')
        v6op3 = types.KeyboardButton('Использовать IDE или IDLE, так же можно писать в CMD и в блокноте')
        markup7.add(v6op1, v6op2, v6op3)
        bot.send_message(message.chat.id, "Как можно писать программы на языке PYTHON", reply_markup=markup7)
    if message.text == "python-xy.github.io":
        markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v6op1 = types.KeyboardButton("Использовать IDE или IDLE")
        v6op2 = types.KeyboardButton('Использовать Word')
        v6op3 = types.KeyboardButton('Использовать IDE или IDLE, так же можно писать в CMD и в блокноте')
        markup7.add(v6op1, v6op2, v6op3)
        bot.send_message(message.chat.id, "Как можно писать программы на языке PYTHON", reply_markup=markup7)
    if message.text == "Использовать IDE или IDLE, так же можно писать в CMD и в блокноте":
        ball = ball + 10
        markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v7op1 = types.KeyboardButton("print")
        v7op2 = types.KeyboardButton('index')
        v7op3 = types.KeyboardButton('adf')
        markup8.add(v7op1, v7op2, v7op3)
        bot.send_message(message.chat.id,
                         "Выберите правильный вариант написание команды которая выводить текст в кансоль",
                         reply_markup=markup8)
    if message.text == "Использовать IDE или IDLE":
        markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v7op1 = types.KeyboardButton("print")
        v7op2 = types.KeyboardButton('index')
        v7op3 = types.KeyboardButton('adf')
        markup8.add(v7op1, v7op2, v7op3)
        bot.send_message(message.chat.id,
                         "Выберите правильный вариант написание команды которая выводить текст в кансоль",
                         reply_markup=markup8)
    if message.text == "Использовать Word":
        markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v7op1 = types.KeyboardButton("print")
        v7op2 = types.KeyboardButton('index')
        v7op3 = types.KeyboardButton('adf')
        markup8.add(v7op1, v7op2, v7op3)
        bot.send_message(message.chat.id,
                         "Выберите правильный вариант написание команды которая выводить текст в кансоль",
                         reply_markup=markup8)
    if message.text == "print":
        ball = ball + 10
        markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v8op1 = types.KeyboardButton("CLion, Microsoft Visual Studio, PyCharm")
        v8op2 = types.KeyboardButton('Microsoft Visual Studio, PyCharm, Sublime Text')
        v8op3 = types.KeyboardButton('Word, Powerpoint, PyCharm')
        markup9.add(v8op1, v8op2, v8op3)
        bot.send_message(message.chat.id, "Выберите список где есть только IDE", reply_markup=markup9)
    if message.text == "index":
        markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v8op1 = types.KeyboardButton("CLion, Microsoft Visual Studio, PyCharm")
        v8op2 = types.KeyboardButton('Microsoft Visual Studio, PyCharm, Sublime Text')
        v8op3 = types.KeyboardButton('Word, Powerpoint, PyCharm')
        markup9.add(v8op1, v8op2, v8op3)
        bot.send_message(message.chat.id, "Выберите список где есть только IDE", reply_markup=markup9)
    if message.text == "adf":
        markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v8op1 = types.KeyboardButton("CLion, Microsoft Visual Studio, PyCharm")
        v8op2 = types.KeyboardButton('Microsoft Visual Studio, PyCharm, Sublime Text')
        v8op3 = types.KeyboardButton('Word, Powerpoint, PyCharm')
        markup9.add(v8op1, v8op2, v8op3)
        bot.send_message(message.chat.id, "Выберите список где есть только IDE", reply_markup=markup9)
    if message.text == "CLion, Microsoft Visual Studio, PyCharm":
        ball = ball + 10
        markup10 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v9op1 = types.KeyboardButton("Linux и Windows")
        v9op2 = types.KeyboardButton('Windows')
        v9op3 = types.KeyboardButton('MacOs, Linux и Windows')
        markup10.add(v9op1, v9op2, v9op3)
        bot.send_message(message.chat.id, "На какие ОС можно установить PYTHON", reply_markup=markup10)

    if message.text == "Microsoft Visual Studio, PyCharm, Sublime Text":
        markup10 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v9op1 = types.KeyboardButton("Linux и Windows")
        v9op2 = types.KeyboardButton('Windows')
        v9op3 = types.KeyboardButton('MacOs, Linux и Windows')
        markup10.add(v9op1, v9op2, v9op3)
        bot.send_message(message.chat.id, "На какие ОС можно установить PYTHON", reply_markup=markup10)

    if message.text == "Word, Powerpoint, PyCharm":
        markup10 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v9op1 = types.KeyboardButton("Linux и Windows")
        v9op2 = types.KeyboardButton('Windows')
        v9op3 = types.KeyboardButton('MacOs, Linux и Windows')
        markup10.add(v9op1, v9op2, v9op3)
        bot.send_message(message.chat.id, "На какие ОС можно установить PYTHON", reply_markup=markup10)
    if message.text == "MacOs, Linux и Windows":
        ball = ball + 10
        print(ball)
        markup11 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v10op1 = types.KeyboardButton("Книжка которая учит писать код")
        v10op2 = types.KeyboardButton('Справочник со всеми командами')
        v10op3 = types.KeyboardButton('Философии программирования')
        markup11.add(v10op1, v10op2, v10op3)
        bot.send_message(message.chat.id, "Что такое Дзен Питона", reply_markup=markup11)
    if message.text == "Windows":
        markup11 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v10op1 = types.KeyboardButton("Книжка которая учит писать код")
        v10op2 = types.KeyboardButton('Справочник со всеми командами')
        v10op3 = types.KeyboardButton('Философии программирования')
        markup11.add(v10op1, v10op2, v10op3)
        bot.send_message(message.chat.id, "Что такое Дзен Питона", reply_markup=markup11)
    if message.text == "Linux и Windows":
        markup11 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        v10op1 = types.KeyboardButton("Книжка которая учит писать код")
        v10op2 = types.KeyboardButton('Справочник со всеми командами')
        v10op3 = types.KeyboardButton('Философии программирования')
        markup11.add(v10op1, v10op2, v10op3)
        bot.send_message(message.chat.id, "Что такое Дзен Питона", reply_markup=markup11)
    if message.text == "Философии программирования":
        ball = ball + 10
        bot.send_message(message.chat.id, "Поздравляем, Вы успешно прошли тестирование👍 ")
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, f'Количество баллов которые вы набрали: {ball}', reply_markup=a)
    if message.text == "Книжка которая учит писать код":
        bot.send_message(message.chat.id, "Поздравляем, Вы успешно прошли тестирование👍 ")
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, f'Количество баллов которые вы набрали: {ball}', reply_markup=a)
    if message.text == "Справочник со всеми командами":
        bot.send_message(message.chat.id, "Поздравляем, Вы успешно прошли тестирование👍 ")
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, f'Количество баллов которые вы набрали: {ball}', reply_markup=a)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print("Error")