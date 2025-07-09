import os

def save_results(
    algoritmo,
    estado_inicial,
    estado_objetivo,
    caminho,
    profundidade,
    nos_expandidos,
    estados_expandidos,
    tempo_exec,
    board_size,
    arvore_gerada=None,
    heuristic=None
):
    # Define a pasta por tamanho do puzzle, ex: data_test/3x3_puzzles
    pasta = f"data_test/{board_size}x{board_size}_puzzles"
    os.makedirs(pasta, exist_ok=True)

    # Monta o nome do arquivo com heurística se aplicável
    if heuristic:
        nome_arquivo = os.path.join(
            pasta, f"{algoritmo.lower()}_{heuristic.lower()}_resolucao.txt"
        )
    else:
        nome_arquivo = os.path.join(
            pasta, f"{algoritmo.lower()}_resolucao.txt"
        )

    with open(nome_arquivo, "w") as f:
        f.write(f"Algoritmo: {algoritmo.upper()}\n")
        if heuristic:
            f.write(f"Heurística usada: {heuristic}\n")
        f.write("\n")

        f.write("Estado inicial:\n")
        f.write(formatar_estado(estado_inicial, board_size))
        f.write("\n\n")

        f.write("Estado objetivo:\n")
        f.write(formatar_estado(estado_objetivo, board_size))
        f.write("\n\n")

        f.write(f"Caminho de ações:\n{caminho}\n\n")
        f.write(f"Número de ações até solução: {len(caminho)}\n")
        f.write(f"Profundidade da solução: {profundidade}\n")
        f.write(f"Número de nós expandidos: {nos_expandidos}\n")
        f.write(f"Quantidade de estados expandidos (distintos): {estados_expandidos}\n")
        f.write(f"Tempo de execução: {tempo_exec:.4f} segundos\n")

        print(arvore_gerada)
        if arvore_gerada:
            f.write("\nÁrvore de busca (transições pai → filho):\n")
            for pai, filho, acao in arvore_gerada:
                if filho == estado_objetivo:
                    f.write(f"*{pai} --[{acao}]--> {filho}*\n")
                f.write(f"{pai} --[{acao}]--> {filho}\n")


        f.write("\n--- FIM ---\n")

def formatar_estado(estado, size):
    linhas = []
    for i in range(size):
        linha = estado[i*size:(i+1)*size]
        linhas.append(" ".join(str(v) for v in linha))
    return "\n".join(linhas)
