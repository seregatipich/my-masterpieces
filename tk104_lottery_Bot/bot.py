import config
import telebot
import random

bot = telebot.TeleBot(config.token)
keyboard_1 = telebot.types.ReplyKeyboardMarkup()


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Да', callback_data=100))
    bot.send_message(message.chat.id, 'Привет! Я - лотерейный бот, ты хочешь начать игру?', reply_markup=markup)

    
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='1', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='2', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='3', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='4', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='5', callback_data=5))


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Круто!')
    answer = ''
    if call.data == '100':
        answer = 'Хорошо, тогда начнём игру в лотерею'

        bot.send_message(call.message.chat.id, answer)

        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='1', callback_data=1))
        markup.add(telebot.types.InlineKeyboardButton(text='2', callback_data=2))
        markup.add(telebot.types.InlineKeyboardButton(text='3', callback_data=3))
        markup.add(telebot.types.InlineKeyboardButton(text='4', callback_data=4))
        markup.add(telebot.types.InlineKeyboardButton(text='5', callback_data=5))
        bot.send_message(call.message.chat.id, 'Выбери одну цифру', reply_markup=markup)  # удалить нужно отсюда
        bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id)
        # play(call)

    if call.data in ['1', '2', '3', '4', '5']:
        win = []
        game = [1, 2, 3, 4, 5]
        for i in range(0, 3):
            index = random.randint(0, len(game) - 1)
            win.append(game[index])
            del game[index]

        if int(call.data) in win:
            bot.send_message(call.message.chat.id, 'Вы выиграли!')
        else:
            bot.send_message(call.message.chat.id, 'Вы проиграли!')


if __name__ == '__main__':
    bot.infinity_polling()
