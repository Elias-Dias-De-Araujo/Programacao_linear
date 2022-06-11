from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

costs = [
    [80, 215],
    [100, 108],
    [102,  68],
]

offers = [1000, 1500, 1200]

demands = [2300, 1400]

# Contando o número de linhas para saber a quantidade de ofertas
num_offer = len(costs)

# Contando o número de colunas para saber a quantidade de demandas
num_demand = len(costs[0])

''' 
    Criando alocação de memória para as variáveis de decisão
    e informando que o seu valor pode várias apenas de 0 a infinito
    atendendo assim a condição de xij >= 0.
'''
x = {}
for i in range(num_offer):
    for j in range(num_demand):
        x[i, j] = solver.IntVar(0, solver.infinity(), '')

# Restrições de oferta
for i in range(num_offer):
    solver.Add(solver.Sum([x[i, j] for j in range(num_demand)]) <= offers[i])

# Restrições de demanda
for j in range(num_demand):
    solver.Add(solver.Sum([x[i, j] for i in range(num_offer)]) >= demands[j])

# Função objetivo
objective = []
for i in range(num_offer):
    for j in range(num_demand):
        objective.append(costs[i][j] * x[i, j])

# Encontrando a solução mínima
solver.Minimize(solver.Sum(objective))

# Invocando solver para resolver o problema
status = solver.Solve()

# Printando resultado do problema
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
    print('Custo total: ', solver.Objective().Value(), '\n')

    for i in range(num_offer):
        for j in range(num_demand):
            print('|Oferta {}º -> Demanda {}º - Quantidade enviada: {}|'.format(
                i + 1, j + 1, x[i, j].solution_value()))
