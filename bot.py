import telebot
import pypyodbc
import sqlite3

Love_users = [438014218, 473966548, 389458875, 738152467, 629143670, 442053967, 601803880, 518766948]

TOKEN = '966816991:AAFSCLWzXFPcGEXTErf9usdMhgGix_MpV-M'
bot = telebot.TeleBot(TOKEN)
commands = {
    '/start: Get used to the bot',
    '/help: Gives you information about the available commands'}
commands = list(commands)
knownUsers = []
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/help', '/start')


@bot.message_handler(commands=['start'])
def command_start(message):
    cid = message.chat.id
    if cid not in knownUsers:
        knownUsers.append(cid)
        bot.send_message(message.chat.id,
                         'Приветсвую тебя мой друг сдесь ты сможешь найти любые формулы по физике,просто напиши её название',
                         reply_markup=keyboard1)
    else:
        bot.send_message(message.chat.id, 'напиши название формулы')


@bot.message_handler(commands=['help'])
def help(message):
    for i in commands:
        bot.send_message(message.chat.id, i)


@bot.message_handler(content_types=['text'])
def get_answer(message):
    try:
        number = message.text
        connect = sqlite3.connect('C:\yandex\data.db')
        cur = connect.cursor()
        request = 'SELECT formula FROM go WHERE name=?'
        result = cur.execute(request, (number,)).fetchone()
        bot.send_message(message.chat.id, result)
        if message.chat.id in i_love_you:
            bot.send_message(message.chat.id, 'Админ просил передать, что любит тебя')
    except Exception as e:
        print(e)
        print(repr(e))
        print(e.args)


bot.polling()
