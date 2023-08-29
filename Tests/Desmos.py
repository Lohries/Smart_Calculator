import matplotlib.pyplot as plt
import numpy as np

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


    plt.plot(x, y, label=f'y = {a}x^2 + {b}x^2 + {c}x^1 + {d}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cubic Function')
    plt.legend()
    plt.grid()
    plt.show()
