import redis
# docker run --name fatorial-python-redis -d -p 6379:6379 redis
#redis_conn.flushdb()

def fatorial_decremento(n):
    if n == 0:
        return 1 
    else:
        return n * fatorial_decremento(n - 1)

def fatorial_incremento(n_inicial, limite):
    if n_inicial > limite:
        return 1
    if n_inicial == 0:
        return 1
    return n_inicial * fatorial_incremento(n_inicial + 1, limite)
    
# Exemplo:
KEY_REDIS = 'fatorial_'  
TTL = 30
numero = 12
resultado_final = 0

redis_conn = redis.Redis(host='localhost', port=6379, decode_responses=True)

valor_redis = redis_conn.get(f'{KEY_REDIS}{numero}')

if(valor_redis is not None):
    print(f'(REDIS) O fatorial de {numero} é: {valor_redis}.')

else:
    numero_aux = numero
    while(numero_aux != 0):
        valor_redis = redis_conn.get(f'{KEY_REDIS}{numero_aux}')

        if(valor_redis is not None):    
            print(f'(REDIS) Encontrou o fatorial de {numero_aux} que é: {valor_redis}.')           
            resultado_parcial = fatorial_incremento(numero_aux + 1, numero)           
            resultado_final = resultado_parcial * int(valor_redis)
            print(f'O fatorial de {numero} é: {resultado_final}.')
            numero_aux = 0
        else:
            numero_aux -= 1
            
    if(valor_redis is None):
        resultado_final = fatorial_decremento(numero) 
        print(f'O fatorial de {numero} é: {resultado_final}.')

    redis_conn.setex(f'{KEY_REDIS}{numero}', TTL, resultado_final)
    




