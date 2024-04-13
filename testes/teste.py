import random

def calcular_pi(num_pontos):
    dentro_circulo = 0
    for _ in range(num_pontos):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x*2 + y*2 <= 1: 
            dentro_circulo += 1
    
    return (dentro_circulo / num_pontos) * 4

num_pontos = 10000000  # 1 bilhão de pontos
pi_aproximado = calcular_pi(num_pontos)
print("Valor aproximado de pi:", pi_aproximado)