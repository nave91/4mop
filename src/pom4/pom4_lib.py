import random

def resetSeed(seed):
    if seed:
        random.seed(seed)
    else:
        random.seed(1)
        

resetSeed(1)
