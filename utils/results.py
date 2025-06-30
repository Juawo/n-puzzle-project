import os
import time

def save_results(algoritmo, estado_inicial, estado_objetivo, caminho, profundidade, nos_expandidos, estados_expandidos, tempo_exec):
    nome_arquivo = f"data_test/{algoritmo.lower()}_resolucao.txt"
    os.makedirs("data_test", exist_ok=True)

    with open(nome_arquivo, "w") as f:
        f.write(f"Algoritmo: {algoritmo}\n\n")
        f.write(f"Estado inicial:\n{estado_inicial}\n\n")
        f.write(f"Estado objetivo:\n{estado_objetivo}\n\n")
        f.write(f"Caminho de ações:\n{caminho}\n\n")
        f.write(f"Número de ações até solução: {len(caminho)}\n")
        f.write(f"Profundidade da solução: {profundidade}\n\n")
        f.write(f"Número de nós expandidos: {nos_expandidos}\n")
        f.write(f"Quantidade de estados expandidos (distintos): {estados_expandidos}\n\n")
        f.write(f"Tempo de execução: {tempo_exec:.4f} segundos\n")
        f.write("\n--- FIM ---\n")
