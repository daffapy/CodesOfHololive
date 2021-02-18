import pyautogui #pip3 install pyautogui 
import time
import os
import pyperclip #pip3 install pyperclip

#Purpose: automating getting the links from every video by just hovering over them and keep the links in your file for the next step.

#WHAT IS AUTOMATED : right-clicking ,  Pasting link and write it on your .txt file , giving delay so you can use your mouse to hover over the title. 

#WHAT IS NOT AUTOMATED : mouse-hovering over the title of the video, copying url

#Loop until you die. Jk, keep looping until you press Ctrl + C (End Program)
while True: #Means while the condition is True / running, it will keep looping the action in this loop
    
    #info : you can change howmany times it will loop by changing 'True' with a variable
    #ex: i = 0
    # while i < 5: (if 'i' is equal to or bigger than 5 then the program will ignore the loop)
    #
    #        do something
    #
    #        i = i + 1  (adding the value of 'i' every time it loops, so it will end after i is equal to 5)
    # will loop for 5 times

    #Accessing .txt files (make sure .txt is in the same directory/folder as the .py file)
    f = open('url_collector.txt','a')#a stands for append 
    time.sleep(1)
    #show notification for debugging (optional) (MacOs only tho)
    os.system("osascript -e 'display notification \"Go!\"\'")
    time.sleep(2)
    #Hover over the title of the video that you want to take the thumbnail
    
    #Auto right-click
    pyautogui.click(button='right')
    #Click Copy Url
    
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
    
    #DaffaXD <3







