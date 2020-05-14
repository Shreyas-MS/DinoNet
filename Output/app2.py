import keyboard
from PIL import ImageGrab
from PIL import Image
import pyautogui
import numpy as np
from keras.models import model_from_json
import cv2
import time

"""overfit4sure = 'D:\\Code\\jumpingChandu\\models\\overfit4sure.h5'
no_val1 = 'D:\\Code\\jumpingChandu\\models\\no_val1.h5'
"""
goodmodel_json_path = 'G:\\2.Real College\\ML_home\\Models\\model2.json'
goodmodel_json_path = "D:\\Machine_Learning\\JumpingChandu\\Model\\goodmodelv7\\model7.json"

def run():
    model_file = open(goodmodel_json_path,'r')
    model = model_file.read()
    model_file.close()
    model = model_from_json(model)
    model.load_weights("D:\\Machine_Learning\\JumpingChandu\\Model\\goodmodelv7\\my_weights_v7.h5")

    while True:
       if keyboard.is_pressed('space'):
            break

    while True:
        img = ImageGrab.grab().resize((384,216)).convert(mode = 'L')

        img = np.array(img)

        img = img[95:150,0:130]
        #tempshow = Image.fromarray(img)
        #tempshow.show()
        #ime.sleep(2)

        # print(img.shape)
        img = np.reshape(img, (-1, 55, 130, 1))

        data = model.predict(img)
        action = np.argmax(data)
        
        print(action)

        if(action == 1):
            jump()
        elif(action == 2):
            duck()

        if keyboard.is_pressed('q'):
            break


def jump():
    """ Quick Jump """
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')   

def duck():
    """ Quick Duck """
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')   


if __name__ == '__main__':
    """ Start control loop """
    run()
