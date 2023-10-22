from telebot.types import Message
from data.loader import bot
from keyboards.default import main_menu_default


@bot.message_handler(commands=['start'], chat_types='private')
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id=chat_id, text=f'Salom, {message.from_user.first_name}!',
                     reply_markup=main_menu_default())

