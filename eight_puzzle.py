from queue import PriorityQueue

# Define a heurística de distância entre as pecas e seus lugares, nesse caso foi usado a distancia Manhattan
def distancia_manhattan(estado):
    distancia = 0
    for i in range(3):
        for j in range(3):
            if estado[i][j] != 0:
                # Calcula a distância horizontal e vertical entre a posição atual e a posição correta
                x, y = divmod(estado[i][j] - 1, 3)
                distancia += abs(x - i) + abs(y - j) # Soma das distâncias horizontal e vertical
    return distancia

# Define a função para gerar os próximos estados possíveis a partir de um estado atual
def proximos_estados_possiveis(estado):
    proximos_estados = []
    linha_zero, coluna_zero = next((i, j) for i, linha in enumerate(estado) for j, val in enumerate(linha) if val == 0)
    for delta_linha, delta_coluna in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nova_linha, nova_coluna = linha_zero + delta_linha, coluna_zero + delta_coluna
        # Verifica se a nova posição está dentro dos limites do tabuleiro
        if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
            # Cria uma cópia do estado atual
            novo_estado = [linha[:] for linha in estado]
            # Move o espaço vazio para a nova posição
            novo_estado[linha_zero][coluna_zero], novo_estado[nova_linha][nova_coluna] = novo_estado[nova_linha][nova_coluna], novo_estado[linha_zero][coluna_zero]
            # Adiciona o novo estado à lista de próximos estados possíveis
            proximos_estados.append(novo_estado)
    return proximos_estados

# Define a função de busca gulosa
def busca_gulosa(estado_incial, objetivo):
    fronteira = PriorityQueue()
    fronteira.put((distancia_manhattan(estado_incial), [estado_incial])) # Adiciona o estado inicial na fila de prioridade
    explorados = set()
    
    while fronteira:
        _, caminho = fronteira.get()  # Pega o próximo estado e o caminho para ele da fila de prioridade
        estado_atual = caminho[-1] # Pega o estado atual do final do caminho
        if (estado_atual == objetivo):
            return caminho
        explorados.add(str(estado_atual)) # Adiciona o estado atual no conjunto de explorados
        for prox_estado in proximos_estados_possiveis(estado_atual):
            if str(prox_estado) not in explorados: # Verifica se o proximo estado ainda não foi explorado
                novo_caminho = caminho + [prox_estado] # Cria um novo caminho adicionando o proximo ao caminho atual
                # Adiciona o novo caminho na fila de prioridade com base na distância de Manhattan
                fronteira.put((distancia_manhattan(prox_estado), novo_caminho))
    return None


# teste
estado_incial = [[1, 6, 3], [2, 0, 5], [4, 7, 8]]
objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

caminho_solucao = busca_gulosa(estado_incial, objetivo)

if caminho_solucao:
    print("Solução encontrada:")
    for i, estado in enumerate(caminho_solucao):
        print("Movimento", i + 1, ":")
        for linha in estado:
            print(linha)
    print("Número de movimentos:", len(caminho_solucao) - 1)
else:
    print("Não foi possível encontrar uma solução.")
