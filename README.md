# NLP-Solves-Hangman
Using an NLP model to try and solve a game of hangman

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

The code runs on python3
you'll need the following libraries

```
pygame
```
which handles the game GUI

and 

```
numpy
```
which was used in Qlearning for building the qtable

```
keras, along with tensorflow backend
```
which was used for building and training the network


### Installing



make sure you have a python3 setup up and running

then to install the needed libraries

```
pip install pygame keras tensorflow numpy
```

to make sure everything is up and running,
```
python main.py
```
this should start a game of hangman pressing the spacebar would have the model predict on the given word.


### Break down into file system and Algorithms used

the code is divided into two parts, the game, and the solver

```
GAME
```
for the game folder settings hold some of the constants and settings used for the GUI.
Hangman holds the code for building the game with pygame GUI.

```
Solver
```
The solver folder contains the building and training of the LSTM model used to play hangman

1)  data.py
        This file holds the preprocessing of the data used to train the model.
        The dataset was downloaded from the American National Corpus. each letter in a given word was given a probabiliy of removal.
        Then the labels are given for every missing letter.



2)  models.py
        This file creates and returns an LSTM model to be used in the training process.
        The goal was to have multiple models and compare their results later.


3)  predict.py
        This file processes the input queries for the model for prediction and returns the predicted answer.
        The characters get turned into their numerical counterparts(ASCII) and then the inverse is done on the prediction,
        the prediction of each letter and its confidence value are returned.

4)  train.py
        This file holds the training function for the project.
        It takes as parameters the paths of the text files of the dataset.
        Reads them line by line and generates the Training X, and y.
        The data is then padded to a length of 25, turned to numerical values and the model is then trained.

### Problem formulation
For the problem, I decided to have the model predict the most possible letter as an aswer.
For example, the word "original", every letter is given a probability of removal, so the dataset could contain everything from
no letters "_ _ _ _ _ _ _ _" to all the letters but one "o r i g i _ a l" where that one letter could be any of them.
A padding of the words was used to make sure all words are accomedated, while making sure to differentiate between a missing letter "_" and a padding " ". Afterwards the word is mapped to every missing letter =>(word,l) for every missing letter l in the word.
Then the model would learn to predict one letter for every word.(assuming the model gave a wrong answer, the second highest confidence level is chosen and so on)



### Running the Agent

Running the main file should have a demo agent predicting some given problems, make sure the data folder has some text files with words to use as corpus.


## DATASET
    http://www.anc.org/data/oanc/download/
