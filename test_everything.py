import pyautogui
import time
import webbrowser
import os
import pyperclip

i = 0

#Loop until you die. Jk, looping until you press Ctrl + C (End Program)
while True:
    #Accessing .txt files
    f = open('url_collector.txt','a')
    time.sleep(1)
    #show notification for debugging (optional)
    os.system("osascript -e 'display notification \"Go!\"\'")
    #Auto right-click
    pyautogui.click(button='right')
    time.sleep(5)
    #making input based on the link that was copied
    inp = pyperclip.paste()
    #Auto write input to .txt files
    f.write(inp + '\n')
    #closing file
    f.close()
    #Notification (optional)
    os.system("osascript -e 'display notification \"Done!\"\'")
    #give delay to move the mouse
    time.sleep(5)







