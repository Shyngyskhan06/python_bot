import os
from telegram.ext import Updater,ConversationHandler,CommandHandler,MessageHandler,Filters

INITIAL, MIDDLE, FINAL = range(3)
def start(bot, updater):
    updater.message.reply_text('Hello')
    return INITIAL


def say_hello(bot, updater):
    updater.message.reply_text('I am in INITIAL state')
    return MIDDLE

def say_howdy(bot,updater):
    updater.message.reply_text('I am in MIDDLE state')
    return FINAL


def say_good_bye(bot,updater):
    updater.message.reply_text('I am in FINAL state, goodbye')


def cancel(bot,updater):
    updater.message.reply_text('Good bye')
    return ConversationHandler.END

def main():
    TOKEN = '889590521:AAGtW7X2N9fVCcegFRo0hoh5WHcefIETrxs'
    updater = Updater(TOKEN)

    dispatcer = updater.dispatcher
    command = CommandHandler('help',help)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states = { INITIAL: [MessageHandler(Filters.text, say_hello),CommandHandler('init', start)],
                   MIDDLE:[MessageHandler(Filters.text, say_howdy)],
                   FINAL: [MessageHandler(Filters.text, say_good_bye)]},
        fallbacks= [CommandHandler('cancel', cancel)]
    )
    dispatcer.add_handler(conv_handler)
    dispatcer.add_handler(command)
    updater.start_polling()
    #updater.start_webhook()
    updater.idle()


if __name__ == '__main__':
    main()