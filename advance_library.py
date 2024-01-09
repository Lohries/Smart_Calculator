import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
import sympy as sp
from tkinter import *

def calculate_sum():
    times = int(input("Quantos numeros: "))
    total = 0
    for i in range(times):
        number = float(input("Numero: "))
        total += number
    print("A resposta é:", total)

def calculate_difference():
    times = int(input("Quantos numeros: "))
    total = 0
    for _ in range(times):
        number = float(input("Numero: "))
        total -= number
    print("A resposta é:", total)

def calculate_product():
    times = int(input("Quantos numeros: "))
    total = 1
    for _ in range(times):
        number = float(input("Numero: "))
        total *= number
    print("A resposta é:", total)

def calculate_quotient():
    numerator = float(input("Digite o numerador: "))
    denominator = float(input("Digite o denominador (não pode ser zero): "))
    if denominator != 0:
        result = numerator / denominator
        print("A resposta é:", result)
    else:
        print("Denominador não pode ser zero.")

def calculate_area():
    shape_type = int(input("Qual figura você quer calcular a área: 1-Quadrado 2-Retângulo 3-Círculo 4-Triângulo 5-Trapezio 6-Triângulo equilátero 7-Heron"))
    if shape_type == 1:
        side = float(input("Digite o lado: "))
        area = side**2
    elif shape_type == 2:
        length = float(input("Digite o comprimento: "))
        width = float(input("Digite a largura: "))
        area = length * width
    elif shape_type == 3:
        radius = float(input("Digite o raio do círculo: "))
        area = math.pi * radius**2
    elif shape_type == 4:
        side = float(input("Digite o lado: "))
        height = float(input("Digite a altura: "))
        area = (side*height)/2
    elif shape_type == 5:
        base_max = float(input("Digite a base maior: "))
        base_min = float(input("Digite a base menor: "))
        height = float(input("Digite a altura: "))
        area = ((base_max + base_min)*height)/2

    elif shape_type == 6:
        side = float(input("Digite o lado: "))
        area = ((side**2)*1.7)/4

    elif shape_type == 7:
        side1 = float(input("Digite o lado 1: "))
        side2 = float(input("Digite o lado 2: "))
        side3 = float(input("Digite o lado 3: "))
        p = (side1+side2+side3)/2
        area1 = p*((p-side1) + (p-side2) + (p-side3))
        area = math.sqrt(area1)


    print(f"A área é: {area}")

def calculate_volume():
    shape_type = int(input("Digite o tipo de sólido: 1-Cubo 2-Pirâmide 3-Cilindro 4-Esfera 5-Outros tipos"))

    if shape_type == 1:
        side = float(input("Digite o lado do cubo: "))
        volume = side**3
    elif shape_type == 2:
        base_area = float(input("Digite a área da base da pirâmide: "))
        height = float(input("Digite a altura da pirâmide: "))
        volume = (base_area * height) / 3
    elif shape_type == 3:
        radius = float(input("Digite o raio do cilindro: "))
        height = float(input("Digite a altura do cilindro: "))
        volume = math.pi * radius**2 * height
    elif shape_type == 4:
        radius = float(input("Digite o raio da esfera: "))
        volume = (4/3) * math.pi * radius**3
    # Adicione outros sólidos conforme necessário...

    print(f"O volume é: {volume}")

def calculate_angles():
    sides = int(input("Quantos lados tem a figura: "))
    if sides > 0:
        total_angle = (sides - 2) * 180
        internal_angle = total_angle / sides
        print(f"A soma dos ângulos internos é {total_angle} graus.")
        print(f"Cada ângulo interno é {internal_angle} graus.")

def calculate_derivative():
    expression = input("Digite a função: ")
    variable = input("Digite a variável: ")

    x = sp.Symbol(variable)
    f = sp.sympify(expression)
    derivative = sp.diff(f, x)

    print(f"A derivada de {expression} em relação a {variable} é:")
    print(derivative)

def calculate_integral():
    def func(x):
        return x**2

    # Calcule a integral definida da função entre os limites [0, 1]
    result, _ = quad(func, 0, 1)
    print("Resultado da integral:", result)

    # Crie um gráfico da função
    x_vals = np.linspace(0, 1, 100)
    y_vals = func(x_vals)
    plt.plot(x_vals, y_vals, label='x^2')
    plt.fill_between(x_vals, y_vals, alpha=0.2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()

# Funções de física
def calculate_weight():
    mass = float(input("Qual a massa (kg): "))
    gravity = float(input("Qual a aceleração devido à gravidade (m/s^2): "))
    weight = mass * gravity
    print(f"O peso é: {weight} Newtons")

def calculate_buoyancy():
    volume_displaced = float(input("Qual o volume deslocado (m^3): "))
    density_fluid = float(input("Qual a densidade do fluido (kg/m^3): "))
    gravity = float(input("Qual a aceleração devido à gravidade (m/s^2): "))
    buoyant_force = volume_displaced * density_fluid * gravity
    print(f"A força de empuxo é: {buoyant_force} Newtons")

def calculate_friction_force():
    normal_force = float(input("Qual a força normal (N): "))
    coefficient_friction = float(input("Qual o coeficiente de atrito: "))
    friction_force = normal_force * coefficient_friction
    print(f"A força de atrito é: {friction_force} Newtons")

def calculate_resultant_force():
    mass = float(input("Qual a massa (kg): "))
    acceleration = float(input("Qual a aceleração (m/s^2): "))
    resultant_force = mass * acceleration
    print(f"A força resultante é: {resultant_force} Newtons")

def graph():
    grau = int(input("Qual o grau da funcao"))
    if grau == 1:
        a = int(input("Digite o coeficiente angular: "))
        b = int(input("Qua termo independente: "))
        precision1 = int(input("Qual a precisao: "))
        precision2 = int(input("Qual a precisao: "))
        precision3 = int(input("Qual a precisao: "))
        x = np.linspace(precision2, precision3, precision1)
        y = a * x**grau + b 
        plt.plot(x, y, label=f'y = {a}x^1 + {b}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Function')
        plt.legend()
        plt.grid()
        plt.show()


    elif grau == 2:
        a = int(input("Digite o coeficiente a: "))
        b = int(input("Digite o coeficiente b: "))
        c = int(input("Qua termo independente: "))

        precision1 = int(input("Qual a precisao: "))
        precision2 = int(input("Qual a precisao: "))
        precision3 = int(input("Qual a precisao: "))

        x = np.linspace(precision2, precision3, precision1)


        y = a * x**grau + b * x + c


        plt.plot(x, y, label=f'y = {a}x^2 + {b}x + {c}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Quadratic Function')
        plt.legend()
        plt.grid()
        plt.show()

    elif grau == 3:
        a = int(input("Digite o coeficiente a: "))
        b = int(input("Digite o coeficiente b: "))
        c = int(input("Digite o coeficiente c: "))
        d = int(input("Qua termo independente: "))

        precision1 = int(input("Qual a precisao: "))
        precision2 = int(input("Qual a precisao: "))
        precision3 = int(input("Qual a precisao: "))

        x = np.linspace(precision2, precision3, precision1)


        y = a * x**grau + b * x**(grau-1)+ c**(grau-2) + d


        plt.plot(x, y, label=f'y = {a}x^3 + {b}x^2 + {c}x^1 + {d}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Cubic Function')
        plt.legend()
        plt.grid()
        plt.show()
    elif grau == 4:
        a = int(input("Digite o coeficiente a: "))
        b = int(input("Digite o coeficiente b: "))
        c = int(input("Digite o coeficiente c: "))
        d = int(input("Digite o coeficiente d : "))
        e = int(input("Qua termo independente: "))

        precision1 = int(input("Qual a precisao (quantidade de pontos a serem desenhados): "))
        precision2 = int(input("Qual o menor valor do dominio: "))
        precision3 = int(input("Qual o maior valor do dominio: "))

        x = np.linspace(precision2, precision3, precision1)


        y = a * x**grau + b * x**(grau-1)+ c**(grau-2) + d(grau-3) + e


        plt.plot(x, y, label=f'y = {a}x^4 + {b}x^3 + {c}x^2 + {d}x^1 + {e}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Quarter Function')
        plt.legend()
        plt.grid()
        plt.show()

