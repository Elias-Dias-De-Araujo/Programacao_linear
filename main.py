import numpy as np
from q1 import q1
from utils import generateProblem

def main():
    i = 0
    print("GERANDO...")
    while (i < 10):
        data = generateProblem()
        x = q1(data[0], data[1], data[2], i)
        x.resolveProblem()
        i += 1
    print("CONCLUIDO!")

if __name__ == "__main__":
    main()

