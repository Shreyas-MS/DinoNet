import keyboard
from PIL import ImageGrab
import numpy as np
import time

# init 
PATH = "D:\Machine_Learning\JumpingChandu\Dataset\\temp"


def run():
    keys = []
    prev = 0
    imgs = []

    while True:
        if keyboard.is_pressed('space'):
            break

    while True:
        img = ImageGrab.grab().resize((384,216)).convert(mode = 'L')
        imgs.append(img)
        print(str(time.time()-prev))
        prev = time.time()

        if keyboard.is_pressed('q'):
            break
        
        if keyboard.is_pressed('space') or keyboard.is_pressed('up'):
            keys.append("\\jump2\\")

        else:
            keys.append("\\nothing\\")
    
    print(len(imgs))
    save(imgs, keys)

def save(imgs, keys):
    """ Save File """
    i = 0
    for key, img in zip(keys, imgs):
        i += 1
        image_PATH = PATH + key +'a'+ str(i) + '.PNG'
        img.save(image_PATH, 'PNG')


if __name__ == '__main__':
    """ Start control loop """
    run()