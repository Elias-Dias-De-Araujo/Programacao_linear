import csv
import time
import numpy as np
from primal import q1
from dual import q2


def generateProblem():
    costs = np.random.randint(100, 999, (100, 100))
    offers = [1]
    demands = [999] #Array inicial apenas para que a condição abaixo aconteça da primeira vez

    while (sum(demands) > sum(offers)):  # Repete enquanto a soma das demandas for maior que as ofertas
        offers = np.random.randint(100, 999, size=100) #Valor minimo do array = 100, Valor máximo do array = 999, Tamanho do array 100
        demands = np.random.randint(100, 999, size=100)

    return (costs, offers, demands)


def main():
    i = 0
    print("GERANDO...")
    header = ['Metodo', 'Solução Encontrada', 'Tempo de execução (ms)']
    file_name = 'results/' + "resultado" + time.strftime("%d-%m-%Y-%H_%M_%S")  + '.csv'
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        while (i < 10):
            data = generateProblem()

            # Primal
            primalTime = time.perf_counter()
            x = q1(data[0], data[1], data[2], i, 'GLOP')
            r1 = x.resolveProblem()
            finalPrimalTime = time.perf_counter()   
            t1 = finalPrimalTime - primalTime

            # Primal ( restrição de integralidade )
            primalTimeRes = time.perf_counter()
            x1 = q1(data[0], data[1], data[2], i, 'SCIP')
            r2 = x1.resolveProblem()
            finalPrimalTimeRes = time.perf_counter()
            t2 = finalPrimalTimeRes - primalTimeRes

            # Dual
            dualTime = time.perf_counter()
            y = q2(data[0], data[1], data[2], i, 'GLOP')
            r3 = y.resolveProblem()
            finalDualTime = time.perf_counter()
            t3 = finalDualTime - dualTime

            # Dual ( restrição de integralidade )
            dualTimeRes = time.perf_counter()
            y1 = q2(data[0], data[1], data[2], i, 'SCIP')
            r4 = y1.resolveProblem()
            finalDualTimeRes = time.perf_counter()
            t4 = finalDualTimeRes - dualTimeRes

            #CRIAÇÃO DO CSV
            writer = csv.writer(f)
            writer.writerow(['ITERAÇÃO: ', i])
            writer.writerow(header)
            writer.writerow(['Primal', r1, t1])
            writer.writerow(['Primal (Restrição de Integralidade)', r2, t2])
            writer.writerow(['Dual', r3, t3])
            writer.writerow(['Dual (Restrição de Integralidade)', r4, t4])
            writer.writerow('')
            
            i += 1
        print("CONCLUIDO!")


if __name__ == "__main__":
    main()
