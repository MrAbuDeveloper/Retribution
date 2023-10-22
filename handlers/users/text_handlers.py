from telebot.types import Message
from data.loader import bot, db


@bot.message_handler(func=lambda message: message.text == 'Buyurtma 🛍')
def reaction_to_order(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id




