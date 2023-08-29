import math

# Suponha que temos um ângulo de 45 graus (convertido para radianos)
angulo_radianos = math.radians(45)

# Funções trigonométricas básicas
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Calculando as funções trigonométricas inversas (arcos)
arcoseno = math.degrees(math.asin(seno))
arcocosseno = math.degrees(math.acos(cosseno))
arcotangente = math.degrees(math.atan(tangente))

# Outras funções trigonométricas
cotangente = 1 / tangente
secante = 1 / cosseno

# Imprimindo os resultados
print(f"Ângulo: {math.degrees(angulo_radianos)} graus")

print(f"Seno: {seno}")
print(f"Cosseno: {cosseno}")
print(f"Tangente: {tangente}")

print(f"Arcoseno: {arcoseno} graus")
print(f"Arcocosseno: {arcocosseno} graus")
print(f"Arcotangente: {arcotangente} graus")

print(f"Cotangente: {cotangente}")
print(f"Secante: {secante}")