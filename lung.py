from telegram.ext import Updater
from telegram.ext import CommandHandler
from teleambu.commands.wiki import wiki_handler
from teleambu.commands.youtube import youtube_handler
from teleambu.commands.urban import urban_handler

updater = Updater(token='1295113065:AAH20oEn9_Wb6HvXErb2SRvMwxAQHPghyiY', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello there! 😀")


start_handler = CommandHandler('start', start)
handlers = [start_handler, wiki_handler, youtube_handler, urban_handler]
for h in handlers:
    dispatcher.add_handler(h)

updater.start_polling()
