
# A Neural net that plays the Chrome dino game

At some point we've all come across this page, you might have tried fixing your internet, or pressing the spacebar to play the game. Me and github.com/prithvianilk, however tried to train a model to play the game by itself.

![Image of chrome dino](https://cdn-images-1.medium.com/max/2000/1*I7Td8zjuH4QWjHbW2WitdA.png)
###### put chrome://dino on chrome to play the game

## Dependencies
* [Python 3.7x](https://www.python.org/)
* [Tensorflow](https://www.tensorflow.org/)
* [Keras](https://keras.io/)
* [Numpy](https://numpy.org/)
* [Pyautogui](https://pypi.org/project/PyAutoGUI/)
* [Keyboard](https://pypi.org/project/keyboard/)

## Data
1. You can use data provided in the [repository](https://github.com/Shreyas-MS/DinoNet/tree/master/Dataset/Train_4) itself or
2. You can get your own data using our [data collection tool](https://github.com/Shreyas-MS/DinoNet/tree/master/Training)

## Model Training
If you're lucky enough to have a powerful local GPU (along with cudatoolkit and Cudnn 10.1) , you can train locally. If you don't you can use cloud services. You could use [this template](https://github.com/Shreyas-MS/DinoNet/tree/master/Pynotebooks) to make your own model or use one of our [previously trained models](https://github.com/Shreyas-MS/DinoNet/tree/master/Model)

Here is a [baseline model](https://github.com/Shreyas-MS/DinoNet/tree/master/Model/goodmodelv2) that was able to get a score of 1200 
These were the performance metrics it achieved:

![loss](https://raw.githubusercontent.com/Shreyas-MS/DinoNet/master/Figures/loss.png)

![precision](https://raw.githubusercontent.com/Shreyas-MS/DinoNet/master/Figures/precision.png)

![recall](https://raw.githubusercontent.com/Shreyas-MS/DinoNet/master/Figures/recall.png)

![auc](https://raw.githubusercontent.com/Shreyas-MS/DinoNet/master/Figures/auc.png)

## Running the model
Use [This script](https://github.com/Shreyas-MS/DinoNet/master/Output) to run your model

### Have Fun!

[Sample video of model playing the game](https://www.youtube.com/watch?v=56pw_7bM2Cg&feature=youtu.be)


[Read this to learn more](https://medium.com/@shreyas75757/a-neural-net-that-plays-the-chrome-dino-game-95c98a61257b)
