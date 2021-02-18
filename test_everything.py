import pyautogui #pip3 install pyautogui 
import time
import os
import pyperclip #pip3 install pyperclip

#Loop until you die. Jk, keep looping until you press Ctrl + C (Windows) or Command + C (MacOs) (End Program)
while True: #Means while the condition is True / running, it will keep looping the action in this loop
    
    #info : you can change howmany times it will loop by changing 'True' with a variable
    #ex: i = 0
    # while i < 5: (if 'i' is equal to or bigger than 5 then the program will ignore the loop)
    #
    #        do something
    #
    #        i = i + 1  (adding the value of 'i' every time it loops, so it will end after i is equal to 5)
    # will loop for 5 times

    #Accessing .txt files
    f = open('url_collector.txt','a')#a stands for append 
    time.sleep(1)
    #show notification for debugging (optional) (MacOs only tho)
    os.system("osascript -e 'display notification \"Go!\"\'")
    #Auto right-click
    pyautogui.click(button='right')
    time.sleep(5)
    #making input based on the link that was copied
    inp = pyperclip.paste()
    #Auto write input to .txt files and change line / inderectly using 'enter' button
    f.write(inp + '\n')
    #closing file
    f.close()
    #Notification (optional)
    os.system("osascript -e 'display notification \"Done!\"\'")
    #give delay to move the mouse
    time.sleep(5)
    #will keep looping again. Simple right? :)







