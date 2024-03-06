import numpy as np
import matplotlib.pyplot as plt

# Definindo a função f(x)
def funcao(x):
    return -x**2 + 4*x

# Definindo a função de vizinhança
def vizinhanca(x, delta):
    return [x - delta, x + delta]

# Definindo o algoritmo de Hill Climbing
def hill_climbing(f, delta, max_iteracoes, valor_inicial):
    pontos_explorados = []  # Lista para armazenar os pontos explorados

    for _ in range(max_iteracoes):
        pontos_explorados.append(valor_inicial)  # Armazenando o ponto explorado

        # Avaliando os valores de f(x) nos pontos vizinhos
        vizinhos = vizinhanca(valor_inicial, delta)
        valores_vizinhos = [f(n) for n in vizinhos]

        # Verificando se há um vizinho com um valor maior de f(x)
        valor_max_vizinho = max(valores_vizinhos)
        if valor_max_vizinho > f(valor_inicial):
            valor_inicial = vizinhos[valores_vizinhos.index(valor_max_vizinho)]
        else:
            break  # Critério de parada: não há melhoria

    return valor_inicial, pontos_explorados

# Executando o algoritmo de Hill Climbing
valor_inicial = 0.5
x_max, x_min = 4, 0
delta = 0.01
max_iteracoes = 1000
max_x, pontos_explorados = hill_climbing(funcao, delta, max_iteracoes, valor_inicial)

# Exibindo o resultado
print("O valor máximo de f(x) encontrado é:", funcao(max_x))
print("O valor de x que maximiza f(x) é:", max_x)

# Plotando a função f(x) e os pontos explorados
valores_x = np.linspace(x_min, x_max, 100)
plt.plot(valores_x, funcao(valores_x), label='f(x) = -x^2 + 4x')
plt.scatter(pontos_explorados, [funcao(x) for x in pontos_explorados], color='red', label='Pontos explorados')
plt.scatter(max_x, funcao(max_x), color='green', label='Máximo encontrado', marker='x', s=100)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Hill Climbing para maximizar f(x)')
plt.legend()
plt.grid(True)
plt.show()
