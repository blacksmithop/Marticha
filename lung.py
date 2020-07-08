from telegram.ext import Updater
from telegram.ext import CommandHandler
from commands.wiki import wiki_handler
from commands.youtube import youtube_handler
from commands.urban import urban_handler
from commands.movie import movie_handler

from os import getenv as e
updater = Updater(token=e('telegram'), use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello there! 😀")


start_handler = CommandHandler('start', start)
handlers = [start_handler, wiki_handler, youtube_handler, urban_handler, movie_handler]
for h in handlers:
    dispatcher.add_handler(h)

updater.start_polling()
