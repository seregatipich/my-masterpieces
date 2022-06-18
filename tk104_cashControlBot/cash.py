import telebot
from telebot import types
import config
from db_manager import first_start_handler, save_user, expense_handler

bot = telebot.TeleBot(config.token)
keyboard_1 = telebot.types.ReplyKeyboardMarkup()

first_start_handler()

expense_name = ''
expense_date = ''


@bot.message_handler(commands=['start'])
def main_menu(message):
    save_user(user_id=message.from_user.id)
    print(message.from_user.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('Add expense')
    button_2 = types.KeyboardButton('Show expenses')
    button_3 = types.KeyboardButton('About')

    markup.add(button_1, button_2, button_3)

    bot.send_message(message.chat.id, f'Alright @{message.from_user.username}, let\'s start!')
    bot.send_message(message.chat.id, 'Choose an option'.format(message.from_user), reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def menu(message):
    if message.text == 'Add expense':
        bot.send_message(message.chat.id, 'Enter expense name')
        bot.register_next_step_handler(message, add_expense_name)

    elif message.text == 'About':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton('What is your name?')
        button_2 = types.KeyboardButton('What were you made for?')
        back = types.KeyboardButton('Go back')
        markup.add(button_1, button_2, back)
        bot.send_message(message.chat.id, 'Choose an option'.format(message.from_user), reply_markup=markup)
    elif message.text == 'Go back':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton('Add expense')
        button_2 = types.KeyboardButton('Show expenses')
        button_3 = types.KeyboardButton('About')
        markup.add(button_1, button_2, button_3)
        bot.send_message(message.chat.id, 'Main menu'.format(message.from_user), reply_markup=markup)
    elif message.text == 'What is your name?':
        bot.send_message(message.chat.id, 'My name is CashControlBot')
    elif message.text == 'What were you made for?':
        bot.send_message(message.chat.id, 'I was made for you')


def add_expense_name(message):
    global expense_name
    expense_name = message.text
    bot.send_message(message.chat.id, 'Enter expense date')
    bot.register_next_step_handler(message, add_expense_date)


def add_expense_date(message):
    global expense_date
    expense_date = message.text
    bot.send_message(message.chat.id, 'Enter expense amount')
    bot.register_next_step_handler(message, add_expense_amount)


def add_expense_amount(message):
    expense_amount = message.text
    expense_handler(expense_name, expense_date, expense_amount)
    bot.send_message(message.chat.id, 'Expense added')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('Add expense')
    button_2 = types.KeyboardButton('Show expenses')
    button_3 = types.KeyboardButton('About')
    markup.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, 'Choose an option'.format(message.from_user), reply_markup=markup)


bot.polling(none_stop=True)
