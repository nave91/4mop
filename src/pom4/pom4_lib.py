import random

def random_estimate(min, cost, max, sprint_length):
    #Normalized Estimate as a function of cost = 30*(cost - min)/(max - min)
    return ((sprint_length*(cost - min))/(max-min)+1)


def resetSeed(seed):
    if seed:
        random.seed(seed)
    else:
        random.seed(1)
        

resetSeed(1)

