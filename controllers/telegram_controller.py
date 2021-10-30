import re
from views.messages import View
from telegram.ext import ConversationHandler
from controllers.pardis_controller import PardisSelenium
import threading


class BotController:
    def __init__(self, update, context):
        self.update = update
        self.context = context

    def get_user_credentials_intro(self):
        get_user_credentials = 1
        self.update.message.reply_text(View.how_to_send_credentials())
        return get_user_credentials

    def get_user_credentials(self):
        text = self.update.message.text
        text_splitted = text.split("\n")
        if len(text_splitted) != 2:
            self.update.message.reply_text(View.signup_failed())
            return False
        username = text_splitted[0]
        password = text_splitted[1]
        self.context.user_data["user_credentials"] = {
            "username": username,
            "password": password,
        }
        self.update.message.reply_text(View.signup_ok())
        return ConversationHandler.END

    def start(self):
        welcome_message = View.welcome()
        self.update.message.reply_text(welcome_message)
        return True

    def go_to_the_class(self):
        if "user_credentials" not in self.context.user_data:
            self.update.message.reply_text(View.credentials_are_required())
            return False
        if "driver" in self.context.user_data:
            self.context.user_data["driver"].close()
            self.context.user_data.pop("driver")

        pardis = PardisSelenium()
        self.context.user_data["driver"] = pardis.driver
        go_to_class = threading.Thread(
            target=pardis.go_to_class,
            args=(self.context.user_data["user_credentials"],),
        )
        go_to_class.start()
        
    def take_screenshot(self):
        if "driver" in self.context.user_data:
            self.update.message.reply_text(self.context.user_data["driver"].current_url)
            self.context.user_data["driver"].save_screenshot("screenshot.png")
            self.update.message.reply_photo(open("screenshot.png", "rb"))
            return True
        return False

    def cancel(self):
        self.update.message.reply_text(View.cancel())
        return ConversationHandler.END