import pyautogui
import pynput
from pynput.keyboard import Listener , Key

#Purpose: To troll your friends so when they type 'space' it will automatically adding 'peko' after it and if they try to delete it, it will add more 'peko'

#function for pressing key
def on_press(key):
    if key == Key.space: #if 'space' was pressed,
        pyautogui.typewrite('peko') #then write 'peko' after it
        #example : a -> a peko (adding peko automatically)
    elif key == Key.backspace: #if you try to delete it,
        pyautogui.typewrite('peko')#it will write more 'peko' hahahaha get rekt peko....
        #example : a peko -> a pek -> a pekpeko (adding peko automatically therefore you cant delete the peko madness)

#To monitor the keyboard
with Listener(on_press=on_press) as listener:
    listener.join()

    #Pain-Peko
    #DaffaXD
    
