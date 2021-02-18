import pyautogui
import time
import webbrowser
import cv2
import os

#your previous .txt files that contains the links
filepath = 'url_collector.txt'
time.sleep(2)

#opening sites
webbrowser.open('http://www.get-youtube-thumbnail.com/')
time.sleep(5)

#reading input from your .txt files
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
           #Clicking the search bar (use YOUR OWN path of the file, dont follow my path if you dont have same path/directory)
           img = os.path.expanduser('~/Documents/search_bar_url.png')
           click_search = pyautogui.locateCenterOnScreen(img,grayscale=True,confidence=.9)
           pyautogui.moveTo(click_search.x/2,click_search.y/2)#for non mac users you dont need to divide the x and y value by 2 (mac is making things harder)
           pyautogui.click()
       time.sleep(1)
       #write
       pyautogui.typewrite(url)
       line = fp.readline()
       #Getting the thumbnail (use YOUR OWN path of the file, dont follow my path if you dont have same path/directory)
       img_2 = os.path.expanduser('~/Documents/get_thumbnail.png')
       click_get = pyautogui.locateCenterOnScreen(img_2,grayscale=True,confidence=.9)
       pyautogui.moveTo(click_get.x/2,click_get.y/2)#for non mac users you dont need to divide the x and y value by 2 (mac is making things harder)
       pyautogui.click()
       #SAVE OR COPY IMAGE BY YOURSELF since im not using selenium, because im lazy (and dont wanna take care of xpath).
       #You can leave it again after copying or saving the file since code below will take care of that
       time.sleep(15)
       #scroll up
       pyautogui.scroll(50)
       time.sleep(2)
       #delete the previous links (use YOUR OWN path of the file, dont follow my path if you dont have same path/directory)
       used_bar = os.path.expanduser('~/Documents/used_search_bar.png')
       delete_search = pyautogui.locateCenterOnScreen(used_bar,grayscale=True,confidence=.9)
       pyautogui.moveTo(delete_search.x/2,delete_search.y/2)#for non mac users you dont need to divide the x and y value by 2 (mac is making things harder)
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

       
