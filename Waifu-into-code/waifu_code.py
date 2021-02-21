from PIL import Image
import os

#Purpose: Making an ASCII Art of your waifu to get her attention (fuckin pathetic)
#run this code on your terminal, and voila an ASCII Art of your waifu's image is made.

# ascii characters used to build the output text (you can add more if you want) (the priority starts from left side)
ASCII_CHARS = ["@", "#", "s", "%", "?", "*", "+", ";", ":", ",", ".","o","d","h","y","m","/","`","-"]

# resize image according to a new width

#change the new_width to your desired width , dont forget to change the new_width on def main too
#(more width = more clear)
def resize_image(image, new_width=200):
    width, height = image.size
    ratio = height/width/1.8 #change the 1.8 if its not proportional 
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

#change the new_width to your desired width, dont forget to change the new_width on def resize_image too
def main(new_width=200):
    # attempt to open image from user-input
    path = os.path.expanduser('~/Documents/moona_img_1.jpg') #use your own path based on the path of your selected image.
    try:
        image = Image.open(path)
        print('ok') #for debugging (optional)
    except:
        print(path, " is not a valid pathname to an image.")
        return
  
    # convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    print(ascii_image)
    
    # save result to "ascii_image.txt" (optional)
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
 
# run program
main()
#Author:
print('\nBy : @DaffaXD')
