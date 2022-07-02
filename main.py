import numpy as np
from q1 import q1
from q2 import q2


def generateProblem():
    costs = np.random.randint(100, 999, (100, 100))
    offers = [1]
    demands = [999]

    while (sum(demands) > sum(offers)):  # Repete enquanto a soma das demandas for maior que as ofertas
        offers = np.random.randint(100, 999, size=100)
        demands = np.random.randint(100, 999, size=100)

    return (costs, offers, demands)


def main():
    i = 0
    print("GERANDO...")
    while (i < 10):
        data = generateProblem()
        # Primal
        x = q1(data[0], data[1], data[2], i)
        x.resolveProblem()

        # Dual
        y = q2(data[0], data[1], data[2], i)
        y.resolveProblem()

        i += 1
    print("CONCLUIDO!")


if __name__ == "__main__":
    main()
