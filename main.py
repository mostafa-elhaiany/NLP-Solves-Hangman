from Solver.data import *
from Solver.models import *
np.random.seed(42)
#reading all the words
words = read_data('data/TheStory.txt')
words += read_data('data/AdamsElissa.txt')
words += read_data('data/ch1.txt')
words += read_data('data/ch2.txt')
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


numerical_hangman_x = get_numerical_data(hangman_x)
print(original_words[102])
print(hangman_x[102])
print(numerical_hangman_x[102])

#setting y to be bounded by 0 1
numerical_hangman_y=np.array([
    Y/np.max(Y) if np.max(Y)>0 else Y for Y in hangman_y
])


#loading model
model = load_model(intput_size=numerical_hangman_x.shape[1])
model.summary()

## training the model
save_best=keras.callbacks.ModelCheckpoint(f"models/model2.h5",
                                                  monitor='val_loss', verbose=1,
                                                  save_best_only=True)

early_stop=keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0,
                                                  patience=20, verbose=1, mode='auto',
                                                  restore_best_weights=True)

model.fit(numerical_hangman_x,numerical_hangman_y,
        batch_size=128,epochs=10,verbose=1,
        validation_split=0.01,
        callbacks=[save_best,early_stop],
         shuffle=True)
 


## loading and using the model
# model = keras.models.load_model('models/model.h5')
# i=random.randint(0,len(numerical_hangman_x)-1)
# word = numerical_hangman_x[i].reshape((1,25,))
# print('what the model sees: \n',word)
# print('what that means: \n',hangman_x[i])
# print('the actual word:  \n',original_words[i])
# p=model.predict(word)
# char = chr(np.argmax(p)+97)
# print('predictions: \n',p)
# print('final output: ',char)