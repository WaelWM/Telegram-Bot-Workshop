import constants as Key
from telegram.ext import *
import responses as R

print("Bot Started!")

def start(update, context):
    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=open("./assets/img.png", "rb"), caption="Welcome to our kidocode workshop telegram bot")
    update.message.reply_text()
    """
    /option
    /start
    /link
    /about
    """

def messageHandler(update, context):
    text = str(update.message.text).lower()
    response = R.responses(text)
    update.message.reply_text(response)

def option(update, context):
    update.message.reply_text(
    """
    /option
    /start
    /link
    /about
    """
    )
    

def error(update, context):
    print(f"update {update} caused error {context.error}")


def link(update, context):
    update.message.reply_text("www.Kidocode.com")

def about(update, context):
    update.message.reply_text("This is a testing bot for telegarm workshop")

def main():
    updater = Updater(Key.API_Key)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('option',option))
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('link',link))
    dp.add_handler(CommandHandler('about',about))

    dp.add_handler(MessageHandler(Filters.text, messageHandler))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()


