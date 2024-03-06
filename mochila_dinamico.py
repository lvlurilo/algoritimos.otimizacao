import pandas as pd

def capacidade_mochila(numero_itens, pesos, valores, capacidade):

    tabela_valor_maximo = [[0 for _ in range(capacidade + 1)] for _ in range(numero_itens + 1)]

    nao_calcula = 0
    calcula = 0
#preenche tabela
    for linha in range(1, numero_itens + 1):
        for coluna in range(1, capacidade + 1):
            if pesos[linha - 1] <= coluna: #calcula apenas se o peso for menor ou igual que o capacidade 
                calcula += 1
                valor_linha_anterior_tabela = tabela_valor_maximo[linha - 1][coluna]
                valor_linha_anterior = valores[linha - 1]
                capacidade_restante = coluna - pesos[linha - 1]
                tabela_valor_maximo[linha][coluna] = max(valor_linha_anterior + tabela_valor_maximo[linha - 1][capacidade_restante], valor_linha_anterior_tabela)
            else:
                nao_calcula += 1
                valor_linha_anterior_tabela = tabela_valor_maximo[linha - 1][coluna]
                tabela_valor_maximo[linha][coluna] = valor_linha_anterior_tabela

# busca os resultados
    itens_incluidos_mochila = []
    pesos_incluidos_mochila = []
    i, j = numero_itens, capacidade
    while i > 0 and j > 0:
        if tabela_valor_maximo[i][j] != tabela_valor_maximo[i - 1][j]:
            itens_incluidos_mochila.append(i - 1)
            pesos_incluidos_mochila.append(pesos[i - 1])
            j -= pesos[i - 1]
        i -= 1

    valor_maximo_encontrado = tabela_valor_maximo[numero_itens][capacidade]

    tabela = pd.DataFrame(tabela_valor_maximo)
    tabela.index =[0, pesos[0], pesos[1], pesos[2], pesos[3], pesos[4], pesos[5]] 

    print(tabela)
    print(f"\nCalculou {calcula} e nao calculou {nao_calcula}. Reaproveitou o valor anterior {round((nao_calcula * 100) / (calcula + nao_calcula), 2)}% das vezes.\n")

    return sum(pesos_incluidos_mochila), valor_maximo_encontrado, itens_incluidos_mochila

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

peso_maximo, valor_maximo, itens_incluidos = capacidade_mochila(len(matriz_ordenada_pesos), pesos, valores, CAPACIDADE)

df = pd.DataFrame({
    'Item': itens,
    'Peso': pesos,
    'Valor': valores
})

df['Included'] = df.index.isin(itens_incluidos)

print("--- Resumo ---")
print("Capacidade Peso:", CAPACIDADE)
print("Soma de Pesos:", peso_maximo)
print("Soma de Valores:", valor_maximo)
print("\n--- Itens Incluidos ---")
print(df[df['Included']][['Item', 'Peso', 'Valor']])
