from cgitb import text
from ortools.linear_solver import pywraplp


class q1():
    def __init__(self, costs, offers, demands, i, solverName):
        self.solver = pywraplp.Solver.CreateSolver(solverName)
        self.costs = costs
        self.offers = offers
        self.demands = demands
        self.iteration = str(i+1)

    def resolveProblem(self):
        # Contando o número de linhas para saber a quantidade de ofertas
        num_offer = len(self.costs)
        # Contando o número de colunas para saber a quantidade de demandas
        num_demand = len(self.costs[0])

        ''' 
            Criando alocação de memória para as variáveis de decisão
            e informando que o seu valor pode várias apenas de 0 a infinito
            atendendo assim a condição de xij >= 0.
        '''

        x = {}
        for i in range(num_offer):
            for j in range(num_demand):
                x[i, j] = self.solver.IntVar(0, self.solver.infinity(), '')

        # Restrições de oferta
        for i in range(num_offer):
            self.solver.Add(self.solver.Sum(
                [x[i, j] for j in range(num_demand)]) <= self.offers[i])

        # Restrições de demanda
        for j in range(num_demand):
            self.solver.Add(self.solver.Sum(
                [x[i, j] for i in range(num_offer)]) >= self.demands[j])

        # Função objetivo
        objective = []
        for i in range(num_offer):
            for j in range(num_demand):
                objective.append(self.costs[i][j] * x[i, j])

        # Encontrando a solução mínima
        self.solver.Minimize(self.solver.Sum(objective))

        # Invocando self.solver para resolver o problema
        status = self.solver.Solve()

        # print(str(self.solver.NumConstraints()))

        # Printando resultado do problema
        if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
            
            return self.solver.Objective().Value()
            """ textfile = open("./results/" + self.folder +
                            "/"+self.iteration+".txt", "w")
            textfile.write('Custo total: {} \n'.format(
                self.solver.Objective().Value())) """
            """ for i in range(num_offer):
                for j in range(num_demand):
                    if (x[i, j].solution_value() > 0):
                        textfile.write('|Oferta {} -> Demanda {} - Quantidade enviada: {}|\n'.format(
                            i + 1, j + 1, x[i, j].solution_value()))

            textfile.write('\n Array de demandas : {} \n Soma das demandas : {} \n'.format(
                self.demands, sum(self.demands)))
            textfile.write('\n Array de ofertas : {} \n Soma das Ofertas: {} \n'.format(
                self.offers, sum(self.offers)))
            textfile.write('\n Matriz de custos : {} \n'.format(self.costs))
            textfile.close() """ 
