# Definição de Node -> Slide Slides 02 - Agentes e Problemas de Busca -> pág 67

class Node:
    
    def __init__(self, state, parent=None, action=None, path_cost=0, depth=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = depth
        self.heuristic = heuristic
    
    def __lt__(self, other):
        return self.path_cost < other.path_cost
   
    def expand(self, problem):
        children = []
        for action in problem.actions(self.state):
            new_state = problem.result(self.state, action)
            cost = problem.pathCost(self.path_cost, self.state, action, new_state)
            child = Node(
                state=new_state,
                parent=self,
                action=action,
                path_cost=cost,
                depth=self.depth + 1
            )
            children.append(child)
        return children

    def solution(self):
        path = []
        node = self
        while node.parent is not None:
            path.append((node.parent.state, node.action))
            node = node.parent
        return list(reversed(path))
    
    def exibir_arvore(self, arvore_busca, board_size):
        """Exibe a árvore de busca com destaque para o caminho da solução."""
        def formatar_estado(estado, size):
            linhas = []
            for i in range(size):
                linha = estado[i * size:(i + 1) * size]
                linhas.append(" ".join(f"{n}" for n in linha))
            return "[" + " | ".join(linhas) + "]"

        caminho_solucao = [(node.state, node.action) for node in self._caminho_solucao_nodes()]
        transicoes_solucao = set()
        for i in range(len(caminho_solucao) - 1):
            pai = caminho_solucao[i][0]
            filho = caminho_solucao[i + 1][0]
            transicoes_solucao.add((pai, filho))

        print("\nÁrvore de Busca Gerada:\n")
        for pai, filho, acao in arvore_busca:
            linha = f"{formatar_estado(pai, board_size)} --[{acao}]--> {formatar_estado(filho, board_size)}"
            if (pai, filho) in transicoes_solucao:
                print("✔ " + linha)
            else:
                print("  " + linha)

    def _caminho_solucao_nodes(self):
        """Retorna a lista de nós do caminho da solução, do início até este nó."""
        node = self
        caminho = []
        while node is not None:
            caminho.append(node)
            node = node.parent
        return list(reversed(caminho))