import sympy as sp

# Definindo a variável e a função
x = sp.Symbol('x')
funcao = x**2 + 2*x + 1

# Calculando a derivada
derivada = sp.diff(funcao, x)

# Exibindo o resultado
print("Função original:", funcao)
print("Derivada:", derivada)