import pyautogui
import pynput
from pynput.keyboard import Listener , Key

#function for pressing key
def on_press(key):
    if key == Key.space: #if 'space' was pressed,
        pyautogui.typewrite('peko') #then write 'peko' after it
    elif key == Key.backspace: #if you try to delete it,
        pyautogui.typewrite('peko')#it will write more 'peko' hahahaha get rekt peko....

with Listener(on_press=on_press) as listener:
    listener.join()

    #Almondo Almondo
    #DaffaXD
    