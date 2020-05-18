import pandas as pd
import numpy as np
import re,random,copy


def read_data(path):
    # f = open(path, "r")
    with open(path, encoding="utf8", mode='r') as f:
        words=[]
        for idx,x in enumerate(f):
            words+=x.split(' ')[1:]
        print(len(words))
    return words


def get_data(words):
    x=[]
    y=[]
    for word in words:
        wordstoList=[]
        if(len(word)==0):
            continue
        alphabet=[0]*26
        word.lower()
        for char in word:
            asci=ord(char)
            if(97<=asci<=122):
                alphabet[asci-97]+=1
                wordstoList.append(char)
            elif(65<=asci<=90):
                alphabet[asci-65]+=1
                wordstoList.append(chr(asci+32))
                
        x.append(wordstoList)
        y.append(alphabet)

    return np.array(x), np.array(y)

def get_hangman_data(x,y):
    new_x=[]
    new_y=[]
    original=[]
    for idx,word in enumerate(x):
        for probability_of_removal in [0.2,0.4,0.6,0.8,1]:
            original.append(word)
            new_word=[]
            word_y=copy.deepcopy(y[idx])  
            for char in word:
                if(char==''):
                    new_word.append(char)
                    continue
                char_position = ord(char)-97
                remove = random.random()<=probability_of_removal
                if(remove):
                    new_word.append('_')
                    word_y[char_position]+1
                else:
                    new_word.append(char)
                    word_y[char_position]=0
            new_x.append(new_word)
            new_y.append(word_y)    
    return np.array(new_x),np.array(new_y),np.array(original)

def get_numerical_data(x):
    new_x=[]
    for idx,word in enumerate(x):
        new_word=[]  
        for char in word:
            if(char==''):
                new_word.append(27)
                continue
            elif(char=='_'):
                new_word.append(28)
                continue
            else:
                char_position = ord(char)-97
                new_word.append(char_position)
        new_x.append(new_word)
    
    return np.array(new_x)




