from os import stat
from random import choice
import re

from telegram.ext import messagehandler

class View:
    @staticmethod
    def welcome():
        message = "سلام. در بتا هستیم. باگ ها طبیعین."
        return message

    @staticmethod
    def how_to_send_credentials():
        message = "در خط اول یوزرنیم یا همون کدملیتو بفرست. تو خط دوم هم پسووردو بده بیاد :)"
        return message

    @staticmethod
    def signup_failed():
        message = "فرمت یوزرنیم پسووردتون صحیح نیست."
        return message

    @staticmethod
    def signup_ok():
        messages = ["اوکی!", "حله!", "عالی!"]
        message = choice(messages)
        return message

    @staticmethod
    def credentials_are_required():
        message = "یوزرنیم پسووردتو نداریم. ساین آپ کن."
        return message

    @staticmethod
    def cancel():
        message = "کنسل گردید."
        return message