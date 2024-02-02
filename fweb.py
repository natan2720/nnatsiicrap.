import requests
from bs4 import BeautifulSoup
from telegram import Bot, Update
from telegram import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging


telegram_token = '6729607780:AAG1r_8oxTRyVQprQtq6T16lSGBMIGrjTho'
chat_id = '562957154'  


website_url = 'https://www.marriott.com/en-us/hotels/addlc-sheraton-addis-a-luxury-collection-hotel-addis-ababa/overview/'


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f"Hello {user.first_name}! Welcome to Sheraton Addis Hotel. "
                              f"Please choose an option from the menu below:\n\n"
                              f"/rooms - Rooms and Services\n"
                              f"/menu - Menu\n"
                              f"/catering - Catering")


def rooms(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Explore our luxurious rooms and services at Sheraton Addis Hotel. "
                              "Visit the website for more details: {}".format(website_url))


def menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Discover our exquisite menu at Sheraton Addis Hotel. "
                              "Visit the website for more details: {}".format(website_url))


def catering(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Plan your catering event with us at Sheraton Addis Hotel. "
                              "Visit the website for more details: {}".format(website_url))


def handle_messages(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("I'm a simple bot and can only respond to specific commands. "
                              "Please use /start to see the menu options.")

def main():
  
    updater = Updater(token=telegram_token)

    dp = updater.dispatcher

   
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rooms", rooms))
    dp.add_handler(CommandHandler("menu", menu))
    dp.add_handler(CommandHandler("catering", catering))

    
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_messages))

   
    updater.start_polling()

    
    updater.idle()


if __name__ == '__main__':
    main()
