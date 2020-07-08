from telegram.ext import CommandHandler
from json import loads
import urllib.request as req


def ud(bot, update):
    if not update.args:
        msg = "Please specify a word to search Urban Dictionary\neg: /ud Yeet"
        return bot.message.reply_text(msg)
    term = ' '.join(update.args)
    url = f"http://api.urbandictionary.com/v0/define?term={term}"
    data = loads(req.urlopen(url=url).read())
    data = data['list'][0]
    msg = f"""*{data['word']}* - {data['author']}\n\n*Description*:\n{data['definition']}\n\n*Example*:\n{data['example']}\n\n{data['thumbs_up']} 👍 {data['thumbs_down']} 👎"""
    return bot.message.reply_markdown(msg)


urban_handler = CommandHandler('ud', ud)
