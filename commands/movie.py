from telegram.ext import CommandHandler
import urllib.request as req
from json import loads
from os import getenv as e


def movie(bot, update):
    if not update.args:
        msg = "Please specify a Movie to search ImDB\neg: /movie Godfather"
        return bot.message.reply_text(msg)
    url = f"http://www.omdbapi.com/?t={'+'.join(update.args)}&apikey={e('omdb')}"
    url = loads(req.urlopen(url=url).read())
    title = url['Title']
    rate = url['Rated']
    run = url['Runtime']
    score = url['imdbRating']
    plot = url['Plot']
    dir = url['Director']
    act = url['Actors']
    award = url['Awards']
    rel = url['Released']
    msg = f"""*{title}* ({rate})\n*Runtime*: {run}\n*Score*: {score}\n*Plot*:\n{plot}\n*Director*: {dir}\n*Actors*: {act}\n*Award*: {award}\n*Released*: {rel}"""
    img = url["Poster"]
    bot.message.reply_photo(img)
    return bot.message.reply_markdown(msg)


movie_handler = CommandHandler('movie', movie)
