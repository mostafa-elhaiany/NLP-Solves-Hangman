import matplotlib.pyplot as plt
def plot(history):
    pass

def train(all_data,plot=False):
    #reading all the words
    print(all_data)
    words=[]
    for path in all_data:
        words += read_data(path)


    #getting the words in X,y numpys
    X,y = get_data(words)
    max_len=25
    x=[]
    for w in X:
        if(len(w)>25):
            continue
        while(len(w)< max_len):
            w.append('')
        w=np.array(w)
        x.append(w)

    x=np.array(x)
    print(x.shape,y.shape)


    #to remove letters and predict the remaining ones
    hangman_x,hangman_y,original_words=get_hangman_data(x,y)
    print(hangman_x.shape)


    #changing the letters to numerical values
    numerical_hangman_x = get_numerical_data(hangman_x)
    print(original_words[102])
    print(hangman_x[102])
    print(numerical_hangman_x[102])

    #setting y to be bounded by 0 1 (sigmoid prediction)
    numerical_hangman_y= copy.deepcopy(hangman_y)
    numerical_hangman_y[numerical_hangman_y!=0]=1
    print(np.min(numerical_hangman_y),np.max(numerical_hangman_y))


    #loading a new model
    model = load_model(intput_size=numerical_hangman_x.shape[1])
    model.summary()


    #setting Callbacks
    save_best=keras.callbacks.ModelCheckpoint(f"models/model.h5",
                                                      monitor='val_loss', verbose=1,
                                                      save_best_only=True)

    early_stop=keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0,
                                                      patience=20, verbose=1, mode='auto',
                                                      restore_best_weights=True)

    # training the model
    history=model.fit(numerical_hangman_x,numerical_hangman_y,
            batch_size=128,epochs=100,verbose=1,
            validation_split=0.01,
            callbacks=[save_best,early_stop],
             shuffle=True)
    if(plot):
        plot(history)

    return model