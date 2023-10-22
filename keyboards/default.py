from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_default():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    order = KeyboardButton('Buyurtma 🛍')
    card = KeyboardButton('Savat 🛒')
    settings = KeyboardButton('Sozlamalar ⚙️')
    feed_back = KeyboardButton('Aloqa 📥')
    markup.add(order, card, feed_back, settings)
    return markup
