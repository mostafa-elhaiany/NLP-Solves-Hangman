import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from Solver.data import *
from Solver.models import *
from Solver.predict import *
from Solver.train import *
from glob import glob
from Game.Hangman import *

#setting random seed for training
np.random.seed(42)

# model=train()
all_data=glob('data/*.txt')
words=[]
for path in all_data:
    words += read_data(path)
gameWords=[]
for i in range(10):
    gameWords.append(words[random.randint(0,len(words)-1)])
# predict('models/model2.h5', 'original','_r_g_nal')

h=Hangman(word='fun', words=gameWords)
model = keras.models.load_model('models/model2.h5')
# h.run()
h.runSolver(model)