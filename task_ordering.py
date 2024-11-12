import random

random.seed(2023402267)

def generate_cost_matrix(n):
    cost_matrix = []
    for i in range(n):
        cost_matrix.append([])
        for j in range(n):
            cost_matrix[-1].append(random.random())
    return cost_matrix

for n in range(6, 12):
    print(generate_cost_matrix(n))