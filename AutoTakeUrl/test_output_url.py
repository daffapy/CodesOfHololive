import pyautogui
import time
import webbrowser
import cv2
import os

filepath = 'url_collector.txt'
time.sleep(2)

webbrowser.open('http://www.get-youtube-thumbnail.com/')
time.sleep(5)

with open(filepath) as fp:
   #reading line by line
   line = fp.readline()
   i = 0
   while line: #while there is still a line with url it will keep looping 
       #deleting whitespace 
       url = line.strip()
       print(url) #for debugging (optional)
       #Locating search bar
       time.sleep(2)
       if i == 0: #i want it only to work once
           img = os.path.expanduser('~/Documents/search_bar_url.png')
           click_search = pyautogui.locateCenterOnScreen(img,grayscale=True,confidence=.9)
           pyautogui.moveTo(click_search.x/2,click_search.y/2)
           pyautogui.click()
       time.sleep(1)
       #write
       pyautogui.typewrite(url)
       line = fp.readline()
       #Getting thumbnail
       img_2 = os.path.expanduser('~/Documents/get_thumbnail.png')
       click_get = pyautogui.locateCenterOnScreen(img_2,grayscale=True,confidence=.9)
       pyautogui.moveTo(click_get.x/2,click_get.y/2)
       pyautogui.click()
       #save or copy the image by yourself since im not using selenium, because im lazy.
       time.sleep(15)
       #scroll up
       pyautogui.scroll(50)
       time.sleep(2)
       #delete the previous links
       used_bar = os.path.expanduser('~/Documents/used_search_bar.png')
       delete_search = pyautogui.locateCenterOnScreen(used_bar,grayscale=True,confidence=.9)
       pyautogui.moveTo(delete_search.x/2,delete_search.y/2)
       pyautogui.click()
       time.sleep(1)
       #Selecting previous link
       pyautogui.keyDown('command')
       pyautogui.press('a')
       pyautogui.keyUp('command')
       time.sleep(1)
       #delete
       pyautogui.press('delete')
       time.sleep(1)
       i = i + 1

       
