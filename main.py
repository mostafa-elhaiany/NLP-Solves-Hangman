from Solver.data import *
from Solver.models import *
from Solver.predict import *
from Solver.train import *
from glob import glob
from Game.Hangman import *

#setting random seed for training
np.random.seed(42)

# model=train(glob('data/*.txt'))
 


# predict('models/model2.h5', 'original','_r_g_nal')

h=Hangman()
h.run()