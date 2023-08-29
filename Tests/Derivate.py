import sympy as sp
import sympy as sym
import math

resposta = input("Quer calcular a derivada? (Sim/Nao): ")
if resposta == "Sim":
    tipo2 = int(input("Qual o tipo: 1-Trigonométrica 2-Algébrica"))
    if tipo2 == 1:
        grau = int(input("Qual o grau: "))
        rad = math.radians(grau)     
        tipo = int(input("Qual o tipo de funcao: 1-seno 2-cos 3-tg"))

        if tipo == 1:
            x = math.cos(rad)
            print(x)
        elif tipo == 2:
            x = math.sin(rad)
            x = x * (-1)
            print(x)

        elif tipo == 3:
            x = math.cos(rad)
            x = pow(x, 2)      
            x = 1/x
            print(x)
    else:
        expression = input("Enter the function: ")
        variable = input("Enter the variable: ")
        
        x = sp.Symbol(variable)
        f = sp.sympify(expression)
        derivative = sp.diff(f, x)

        print("The derivative of", expression, "with respect to", variable, "is:")
        print(derivative)                  

else:
    print("Ate Mais")
    exit()
