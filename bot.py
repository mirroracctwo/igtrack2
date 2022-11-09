import logging
import api , scrape
from telegram import Update
from telegram.ext import CommandHandler,CallbackContext,Updater


#Enable Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = api.api_key

def start(update: Update,context: CallbackContext):
    update.message.reply_text("Hello")

def getdetail(update: Update,context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text = f"Processing...")
    scrape.send_message(0)


def main():

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    #handlers from dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("getdetail", getdetail))

    #Start Polling and wait for any signal to end the program
    logger.info("Started Polling...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
    scrape.send_message(1800)


