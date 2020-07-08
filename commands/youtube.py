from telegram.ext import CommandHandler
from youtubesearchpython import searchYoutube
from json import loads


def yt(bot, update):
    if not update.args:
        msg = "Please specify a keyword to search Youtube\neg: /yt Wake Me Up"
        return bot.message.reply_text(msg)
    query = ' '.join(update.args)
    res = searchYoutube(query, offset=1, mode="json", max_results=1)
    res = loads(res.result())['search_result'][0]
    msg = f"""*{res['title']}*\n*Channel* : {res['channel']}\n*Dur* : {res['duration']}\n\n[Video]({res['link']})"""
    return bot.message.reply_markdown(msg)


youtube_handler = CommandHandler('yt', yt)
