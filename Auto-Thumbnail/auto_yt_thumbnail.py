from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import os
import sys

#============================================= Declaring Functions and driver =================================================

#path to your driver (mine is chromedriver)
PATH = os.path.expanduser("chromedriver")
driver = webdriver.Chrome(executable_path=PATH)
time.sleep(1)

#Go to moonahoshinova's channel
driver.get("https://www.youtube.com/channel/UCP0BspO_AMEe3aQqqpo89Dg/videos")

def collectLinks():
    #variable declaration
    hm_links = 0
    wait_get_link = 0
    elements = []
    ht=driver.execute_script("return document.documentElement.scrollHeight;")
    
    #Go to bottom of the page first (to load all videos)
    while True:
        #basically auto scrolling
        prev_ht=driver.execute_script("return document.documentElement.scrollHeight;")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)
        ht=driver.execute_script("return document.documentElement.scrollHeight;")
        if prev_ht==ht:
            break

    #Find , Count and Put the links into your .txt file (mine is youtube_links.txt)
    elems = driver.find_elements_by_xpath('//*[@id="video-title"]')
    print("Collecting links...")
    for elem in elems:
        elements.append(str(elem.get_attribute("href")))
    f = open("youtube_links.txt",'w')

    for i in elements:
        if 'videos' in i:
            continue
        elif "watch" in i:
            f.write(i)
            f.write("\n")
            hm_links = hm_links + 1
        print(i)
    print("There is " + str(hm_links) + " Links Collected.")
    f.close()
    print("\n")

def collectThumbnail():
    print("Collecting Thumbnail\n\n")
    #go to the site
    driver.get("http://www.get-youtube-thumbnail.com/")
    time.sleep(5)
    with open("youtube_links.txt","r") as al:
        a = 0
        for line in al: #while there is still a line with url in it, it will keep looping 
            a = a + 1
            time.sleep(2)
            #deleting whitespace 
            url = line.strip()
            sys.stdout.write(url + "\n") #for debugging (optional)

            #find search bar and type the links in it
            inp = driver.find_elements_by_id('youtubeLink')[0]
            inp.send_keys(url)
            time.sleep(1)

            #clicking the button to show the thumbnails
            btn = driver.find_elements_by_id("get")[0]
            btn.click()
            time.sleep(1)

            #scrolling to see the thumbnails
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)

            #right-clicking on the image
            img = driver.find_element_by_xpath("//*[@class='image']")
            actionChains = ActionChains(driver)
            actionChains.context_click(on_element=img).perform()

            #Save or Copy by yourself since it is impossible to automate that unless you use/understand pyautogui

            time.sleep(5) #Give the delay for you to copy / save the image, you can change the delay to whatever you like.

            #refreshing page for the next input/url
            driver.refresh()
        print(a) #for debug to show howmany url has been transported (optional)

#=============================================== Calling Fuctions ========================================================
collectLinks()
time.sleep(10)
collectThumbnail()

#quitting the driver and ending the program :)
driver.quit()

