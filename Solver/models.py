import keras
from keras.models import Sequential,Model,load_model
from keras.layers import Dense,Dropout,Embedding,Bidirectional,LSTM,Input


def load_model(intput_size,output_size=26,vocab_size=29 ,embedding_dim=16 ,lstm_filter=26):
    model = Sequential()
    model.add(Embedding(vocab_size, embedding_dim,input_length=intput_size))
    model.add(Bidirectional(LSTM(lstm_filter,return_sequences=True)))
    model.add(Bidirectional(LSTM(lstm_filter)))
    model.add(Dense(50,activation='relu'))
    model.add(Dense(output_size,activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    return model
