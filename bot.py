from data.loader import bot, db
from middlewares.antiflood import SimpleMiddleware

import handlers


def create_tables():
    pass


bot.setup_middleware(SimpleMiddleware(0.6))

if __name__ == '__main__':
    create_tables()
    bot.infinity_polling()
