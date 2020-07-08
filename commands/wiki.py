from telegram.ext import CommandHandler
from wikipediaapi import Wikipedia

wikipedia = Wikipedia('en')


def wiki(bot, update):
    if not update.args:
        msg = "Please specify a topic to search Wikipedia\neg: /wiki Water"
        return bot.message.reply_text(msg)
    result = wikipedia.page(' '.join(update.args))
    if not result.exists():
        msg = "Could not find a Wikipedia article on that Topic"
        return bot.message.reply_text(msg)
    msg = f"""*{result.title}*\n\n{result.text[0:500]}...\n[Page]({result.fullurl})"""
    return bot.message.reply_markdown(msg)


wiki_handler = CommandHandler('wiki', wiki)
