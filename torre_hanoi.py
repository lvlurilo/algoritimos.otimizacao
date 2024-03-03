def torre_hanoi(num_discos, origem, destino, auxiliar):
    if num_discos == 1:
        print(f"Move o disco 1 da {origem} para {destino}")
        return
    torre_hanoi(num_discos - 1, origem, auxiliar, destino)
    print(f"Move o disco {num_discos} da {origem} para {destino}")
    torre_hanoi(num_discos - 1, auxiliar, destino, origem)

N_DISCOS = 3

print('Numero de discos', N_DISCOS)
torre_hanoi(N_DISCOS, 'torre A', 'torre C', 'torre B')