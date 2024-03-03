import random

# Função para inicializar uma população aleatória
def inicializar_populacao(tamanho_populacao, tamanho_individuo):
    return [[random.randint(0, 1) for _ in range(tamanho_individuo)] for _ in range(tamanho_populacao)]

# Função para avaliar o fitness de um indivíduo
def avaliar_fitness(individuo, valores, pesos, capacidade):
    valor_total = 0
    peso_total = 0
    for i in range(len(individuo)):
        if individuo[i] == 1:
            valor_total += valores[i]
            peso_total += pesos[i]
            if peso_total > capacidade:
                return 0  # Se o peso total exceder a capacidade, retorna fitness 0
    return valor_total

# Função para estimar a distribuição de probabilidade
def estimar_distribuicao(populacao):
    distribuicao = [sum(individuo) / len(individuo) for individuo in zip(*populacao)]
    return distribuicao

# Função para crossover usando distribuição de probabilidade
def crossover_com_distribuicao(pai1, pai2, distribuicao):
    ponto_corte = random.choices(range(len(pai1)), weights=distribuicao, k=1)[0]
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

# Função para seleção de pais (torneio)
def selecao_pais(populacao, valores, pesos, capacidade):
    torneio = random.sample(populacao, 3)  # Seleciona 3 indivíduos aleatórios para o torneio
    torneio.sort(key=lambda x: avaliar_fitness(x, valores, pesos, capacidade), reverse=True)
    return torneio[0]

# Função para mutação (invertendo um bit aleatório)
def mutacao(individuo):
    indice_mutacao = random.randint(0, len(individuo) - 1)
    individuo[indice_mutacao] = 1 if individuo[indice_mutacao] == 0 else 0
    return individuo

# Algoritmo Genético para resolver o problema da mochila
def algoritmo_genetico(valores, pesos, capacidade, tamanho_populacao, num_geracoes):
    populacao = inicializar_populacao(tamanho_populacao, len(valores))
    distribuicao = estimar_distribuicao(populacao)

    for _ in range(num_geracoes):
        nova_populacao = []

        for _ in range(tamanho_populacao // 2):
            pai1 = selecao_pais(populacao, valores, pesos, capacidade)
            pai2 = selecao_pais(populacao, valores, pesos, capacidade)
            filho1, filho2 = crossover_com_distribuicao(pai1, pai2, distribuicao)
            filho1 = mutacao(filho1) if random.random() < 0.1 else filho1  # Taxa de mutação de 10%
            filho2 = mutacao(filho2) if random.random() < 0.1 else filho2
            nova_populacao.extend([filho1, filho2])

        populacao = nova_populacao
        distribuicao = estimar_distribuicao(populacao)

    melhor_individuo = max(populacao, key=lambda x: avaliar_fitness(x, valores, pesos, capacidade))
    melhor_valor = avaliar_fitness(melhor_individuo, valores, pesos, capacidade)
    return melhor_individuo, melhor_valor

# Exemplo de uso | item | peso | valor |:
matriz = [
    ['saco de dormir', 15,15],
    ['corda', 3,7],
    ['canivete',2,10],
    ['tocha',5,5],
    ['garrafa',9,8],
    ['comida',20,17]
] 

matriz_ordenada_pesos = sorted(matriz, key=lambda x: x[1], reverse=False)
itens = [linha[0] for linha in matriz_ordenada_pesos]
pesos = [linha[1] for linha in matriz_ordenada_pesos]
valores = [linha[2] for linha in matriz_ordenada_pesos]
CAPACIDADE = 30

TAMANHO_POPULACAO = 50
NUM_GERACOES = 100

melhor_individuo, melhor_valor = algoritmo_genetico(valores, pesos, CAPACIDADE, TAMANHO_POPULACAO, NUM_GERACOES)
print("Melhor solução encontrada:", melhor_individuo)
print("Valor total:", melhor_valor)
