import sympy as sp
import math

Resposta = input("Qual calculo deseja que possa ser executado: 1-Soma    2-Menos    3-Divisao   4-Multiplicacao    5-Areas de Figuras plana   6-Formulas Fisica   7-Angulos    8-Areas de Solidos Geometricos    9-Volume    10-Derivadas     11-Integrais")
Resposta = int(Resposta)


if Resposta == 1:
    vezes = input  ("Quantos numeros: ")
    numero = 0
    numero = int(numero)
    while vezes <= 0:

        numero2 = input("Numero: ")
        numero2 = int(numero)
        numero = numero2 + numero
        vezes = vezes - 1
    
    print("A resposta é de")
    print(numero)



elif Resposta == 2:
    vezes = input  ("Quantos numeros: ")
    numero = 0
    numero = int(numero)
    while vezes <= 0:

        numero2 = input("Numero: ")
        numero2 = int(numero)
        numero = numero2 - numero
        vezes = vezes - 1
    
    print("A resposta é de")
    print(numero)



elif Resposta == 3:
    vezes = input  ("Quantos numeros: ")
    numero = 0
    numero = int(numero)
    while vezes <= 0:

        numero2 = input("Numero: ")
        numero2 = int(numero)
        numero = numero2 / numero
        vezes = vezes - 1
    
    print("A resposta é de")
    print(numero)




elif Resposta == 4:
    vezes = input  ("Quantos numeros: ")
    numero = 0
    numero = int(numero)
    while vezes <= 0:

        numero2 = input("Numero: ")
        numero2 = int(numero)
        numero = numero2 * numero
        vezes = vezes - 1
    
    print("A resposta é de")
    print(numero)





elif Resposta == 5:
    Resposta_2 = input("Qual figura vc quer calcular a area: 1-Quadrado 2-Retangulo 3-Circulo 4-Triangulo 5-Trapézio 6-Triangulo equilatero 7-Heron")
    if Resposta_2 == 1:
        lado = input("Digite o lado: ")
        lado = int(lado)
        area = pow(lado, 2)
        

    elif Resposta_2 == 2:
        lado = input("Digite o lado: ")
        altura = input("Digite a altura: ")
        lado = int(lado)
        altura = int(altura)
        area = lado * altura

    
    elif Resposta_2 == 3:
        raio = input("Qual o raio do circulo: ")
        raio = int(raio)
        area = pow(2,raio) * math.pi


    elif Resposta_2 == 4:
        lado = input("Qual o lado: ")
        lado = int(lado)
        altura = input("Qual a altura")
        altura = int(altura)
        area = (lado * altura)/2
    

    elif Resposta_2 == 5:
        base = input("Qual a base menor: ")
        base = int(base)
        base_M = input("Qual a base maior: ")
        base_M = int(base_M)
        altura = input("Qual a altura: ")
        altura = int(altura)
        area = (base + base_M) * altura
        area = int(area)
        area = area/2

    elif Resposta_2 == 6:
        lado = input("Qual o lado: ")
        area = (pow(2, lado) * math.sqrt(3))/4
    


    elif Resposta_2 == 7:
        lado1 = input("Digite um lado: ")
        lado2 = input("Digite outro lado: ")
        lado3 = input("Digite outro lado: ")
        lado1, lado2, lado3 = int(lado1, lado2, lado3)
        semi = lado1 + lado2 + lado3
        area = semi * (semi - lado1) * (semi - lado2) * (semi - lado3)
        area = math.sqrt(area)


    
    print(area)

        



elif Resposta == 6:
    print("Digite qual formula fisica deseja usar: 1-Peso 2-Empuxo 4-Resultante 5-Elastica 6-Tensao e Normal 7-Velocidade Media 8-Aceleracao 9-Funcao do Espaço(MU) 10-Funcao do Espaço MUV 11-Funcao da velocidade MUV 12-Força Magnética 13-Força Elétrica 14-Momento Linear 15- ")




elif Resposta == 7:




elif Resposta == 8:




elif Resposta == 9:

