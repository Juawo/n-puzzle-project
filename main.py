from core.problem import Problem
from core.node import Node

# Estado inicial simples (0 é o espaço vazio)
estado_inicial = (1, 2, 3,
                  4, 0, 5,
                  6, 7, 8)

# Estado objetivo (padrão do puzzle 8)
estado_objetivo = (1, 2, 3,
                   4, 5, 6,
                   7, 8, 0)

# Criar o problema
puzzle = Problem(estado_inicial, estado_objetivo, board_size=3)

# Criar nó raiz
no_inicial = Node(estado_inicial)

# Expandir o nó inicial
filhos = no_inicial.expand(puzzle)

# Mostrar os filhos gerados
print("EXPANSÃO DO NÓ INICIAL:")
for filho in filhos:
    print(f"Ação: {filho.action}")
    print(f"Estado: {filho.state}")
    print(f"Custo acumulado: {filho.path_cost}")
    print(f"Profundidade: {filho.depth}")
    print("-" * 30)
