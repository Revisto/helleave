from telegram import Update
from telegram.ext import CallbackContext

from controllers.telegram_controller import BotController


def start_and_help(update: Update, context: CallbackContext) -> int:
    return BotController(update, context).start()
    
def go_to_class_now(update: Update, context: CallbackContext) -> int:
    return BotController(update, context).go_to_the_class()

def get_user_credentials_intro(update: Update, context: CallbackContext) -> int:
    return BotController(update, context).get_user_credentials_intro()

def get_user_credentials(update: Update, context: CallbackContext) -> int:
    return BotController(update, context).get_user_credentials()

def take_screenshot(update: Update, context: CallbackContext) -> int:
    return BotController(update, context).take_screenshot()

def cancel(update: Update, context: CallbackContext) -> int:
    return BotController(update, context).cancel()