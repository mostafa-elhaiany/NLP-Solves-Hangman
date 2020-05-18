import keras
import numpy as np
def predict(model_path, original_word, to_be_predicted,max_len=25):
    # loading and using the model
    model = keras.models.load_model(model_path)
    word=[]
    for char in to_be_predicted:
        asci=ord(char)
        if(97<=asci<=122):
            word.append(asci-97)
        elif(65<=asci<=90):
            word.append(asci-65)
        elif(char=='_'):
            word.append(28)
    while(len(word)<max_len):
        word.append(28)
    word=np.array(word)
    print('what the model sees: \n',word)
    print('what that means: \n',to_be_predicted)
    print('the actual word:  \n',original_word)
    p=model.predict(word.reshape((1,max_len)))[0]
    print('predictions: ')
    for idx,c in enumerate(p):
        print(f'{chr(idx+97)}: {np.rint(c*100)}%',end=', ')
    print()
    char = chr(np.argmax(p)+97)
    print('final output: ',char)
    print('========================')