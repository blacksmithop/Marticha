from telegram.ext import CommandHandler


def poll(bot, update):
    if not update.args:
        return bot.reply_text("Create a poll\nQuestion, Option1, Option2...")
    query = ' '.join(update.args)
    query = query.split(',')
    if len(query) <=2:
        return bot.reply_text("Poll must've atleast 2 Options")
    return bot.message.reply_poll(query[0], query[1:], is_anonymous=False, allows_multiple_answers=False)


def dice(bot, update):
    return bot.message.reply_dice(timeout=3)


dice_handler = CommandHandler('dice', dice)
poll_handler = CommandHandler('poll', poll)
