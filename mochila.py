# Função recursiva para resolver o problema da mochila
def capacidade_mochila(valores, pesos, capacidade, qtdade_itens):
    # Se não houver mais itens ou a capacidade da mochila for zero
    if qtdade_itens == 0 or capacidade == 0:
        return 0

    # Se o peso do último item for maior que a capacidade da mochila, exclue o item
    if pesos[qtdade_itens-1] > capacidade:
        return capacidade_mochila(valores, pesos, capacidade, qtdade_itens-1)

    # Retorne o máximo entre incluir ou excluir o item atual
    return max(valores[qtdade_itens-1] + capacidade_mochila(valores, pesos, capacidade-pesos[qtdade_itens-1], qtdade_itens-1), 
               capacidade_mochila(valores, pesos, capacidade, qtdade_itens-1))

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

valor_maximo = capacidade_mochila(valores, pesos, CAPACIDADE, len(matriz_ordenada_pesos))
print("Valor máximo colocado na mochila:", valor_maximo)
