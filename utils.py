import numpy as np


def generateProblem():
    costs = np.random.randint(100, 999, (100, 100))
    offers = [1]
    demands = [999]
    
    while (sum(demands) > sum(offers)): #Repete enquanto a soma das demandas for maior que as ofertas
        offers = np.random.randint(100, 999, size=100)
        demands = np.random.randint(100, 999, size=100)
    
    return (costs, offers, demands)