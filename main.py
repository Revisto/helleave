from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler
)

from handlers.handler import *
from config import Config

GET_CREDENTIALS = 1

def main() -> None:
    updater = Updater(Config.token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(["start", "help"], start_and_help))
    dispatcher.add_handler(CommandHandler(["screenshot", "ss", "status"], take_screenshot))
    dispatcher.add_handler(CommandHandler(["go", "got_to_my_class"], go_to_class_now))
    signup_converstation = ConversationHandler(
        entry_points=[CommandHandler(["signup"], get_user_credentials_intro)],
        states={
            GET_CREDENTIALS: [
                MessageHandler(Filters.text, get_user_credentials)
            ]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    dispatcher.add_handler(signup_converstation)


    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
