import sympy as sp
import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from scipy.integrate import quad




Resposta = input("Qual calculo deseja que possa ser executado: 1-Soma    2-Menos    3-Divisao   4-Multiplicacao    5-Areas de Figuras plana   6-Formulas Fisica   7-Angulos    8-Areas de Solidos Geometricos    9-Volume    10-Derivadas     11-Integrais 12-Calculadora grafica")
Resposta = int(Resposta)


if Resposta == 1:
    vezes = int(input("Quantos numeros: "))
    numero = 0
    numero = int(numero)
    while vezes >= 0:

        numero2 = input("Numero: ")
        numero2 = int(numero)
        numero = numero2 + numero
        vezes = vezes - 2
    
    print("A resposta é de")
    print(numero)



elif Resposta == 2:
    vezes = int(input("Quantos numeros: "))
    numero = 0
    numero = int(numero)
    while vezes <= 0:

        numero2 = input("Numero: ")
        numero2 = int(numero)
        numero = numero2 - numero
        vezes = vezes - 2
    
    print("A resposta é de")
    print(numero)



elif Resposta == 3:
    vezes = int(input("Quantos numeros: "))
    numero = 0
    numero = int(numero)
    while vezes <= 0:

        numero2 = input("Numero: ")
        numero2 = int(numero)
        numero = numero2 / numero
        vezes = vezes - 2
    
    print("A resposta é de")
    print(numero)




elif Resposta == 4:
    vezes = int(input("Quantos numeros: "))
    numero = 0
    numero = int(numero)
    while vezes <= 0:

        numero2 = input("Numero: ")
        numero2 = int(numero)
        numero = numero2 * numero
        vezes = vezes - 2
    
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
    print("Digite qual formula fisica deseja usar: 1-Peso 2-Empuxo 3-Atrito 4-Resultante 5-Elastica 6-Tensao e Normal 7-Velocidade Media 8-Funcao do Espaço(MU) 9-Aceleracao 10-Funcao do Espaço MUV 11-Funcao da velocidade MUV 12-Força Magnética 13-Força Elétrica 14-Momento Linear 15-Torque 16-Velocidade de uma onda 17-Comprimento de uma onda 18-Frequencia de uma onda 19-Corrente eletrica 20-Tensao elétrica")
    Resposta_3 = input("Qual formula: ")
    if Resposta_3 == 1:
        massa = input("Qual a massa: ")
        massa = int(massa)
        gravidade = input("Qual a gravidade: ")
        gravidade = int(gravidade)
        peso = massa * gravidade



    elif Resposta_3 == 2:
        volume = input("Qual o volume deslocado: ")
        volume = int(volume)
        densidade = input("Qual a densidade do fluido: ")
        densidade = int(densidade)
        gravidade = input("Qual a gravidade: ")
        gravidade = int(gravidade)
        força = volume * gravidade * densidade



    elif Resposta_3 == 3:
        normal = input("Qual a força normal (lembrando ela pode ser igual a peso): ")
        normal = int(normal)
        coeficiente = input("Qual o coeficiente de atrito (estatico ou dinamico): ")
        coeficiente = int(coeficiente)
        força = normal * coeficiente





    elif Resposta_3 == 4:
        massa = input("Qual a massa: ")
        aceleracao = input("Qual a aceleracao: ")
        massa = int(massa)
        aceleracao = int(aceleracao)
        forca = massa * aceleracao

        





    elif Resposta_3 == 5:
        constante = input("Qual a constante: ")
        constante = int(constante)
        x = input("Qual a deformacao em metros: ")
        x = int(x)
        força = x * constante



    elif Resposta_3 == 6:
        print("Normal é oposto a força peso em superficie plana e tensao é definida conforme existir um tencionamento na corda")




    elif Resposta_3 == 7:
        distancia_percorrida = float(input("Digite a distância percorrida (metros): "))
        tempo_decorrido = float(input("Digite o tempo decorrido (segundos): "))
        velocidade_media = distancia_percorrida / tempo_decorrido
        print(f"A velocidade média é {velocidade_media:.2f} m/s")




    elif Resposta_3 == 8:
        velocidade_movimento_uniforme = float(input("Digite a velocidade do movimento uniforme (m/s): "))
        tempo_decorrido = float(input("Digite o tempo decorrido (segundos): "))
        espaco_inicial = float(input("Qual o espaço inicial"))
        espaco_percorrido = (velocidade_movimento_uniforme * tempo_decorrido) + espaco_inicial
        print(f"O espaço percorrido é {espaco_percorrido:.2f} metros")



    elif Resposta_3 == 9:
        variacao_velocidade = float(input("Digite a variação da velocidade (m/s²): "))
        tempo_decorrido = float(input("Digite o tempo decorrido (segundos): "))

        aceleracao = variacao_velocidade / tempo_decorrido
        print(f"A aceleração é {aceleracao:.2f} m/s²")


    elif Resposta_3 == 10:
        velocidade_inicial = float(input("Digite a velocidade inicial (m/s): "))
        aceleracao = float(input("Digite a aceleração (m/s²): "))
        tempo_decorrido = float(input("Digite o tempo decorrido (segundos): "))
        posicao = velocidade_inicial * tempo_decorrido + 0.5 * aceleracao * tempo_decorrido ** 2
        print(f"A posição é {posicao:.2f} metros")


    elif Resposta_3 == 11:
        velocidade_inicial = float(input("Digite a velocidade inicial (m/s): "))
        aceleracao = float(input("Digite a aceleração (m/s²): "))
        tempo_decorrido = float(input("Digite o tempo decorrido (segundos): "))

        velocidade = velocidade_inicial + aceleracao * tempo_decorrido
        print(f"A velocidade é {velocidade:.2f} m/s")


    elif Resposta_3 == 12:
        carga_particula = float(input("Digite a carga da partícula (Coulombs): "))
        velocidade_particula = float(input("Digite a velocidade da partícula (m/s): "))
        campo_magnetico = float(input("Digite o campo magnético (Tesla): "))
        forca_magnetica = carga_particula * velocidade_particula * campo_magnetico
        print(f"A força magnética é {forca_magnetica:.2e} N")


    elif Resposta_3 == 13:
        carga1 = float(input("Digite a carga da primeira partícula (Coulombs): "))
        carga2 = float(input("Digite a carga da segunda partícula (Coulombs): "))
        distancia = float(input("Digite a distância entre as partículas (metros): "))
        constante_k = 8.99e9  # Constante eletrostática em N m²/C²
        forca_eletrica = constante_k * (carga1 * carga2) / distancia ** 2
        print(f"A força elétrica é {forca_eletrica:.2e} N")



    elif Resposta_3 == 14:
        massa_objeto = float(input("Digite a massa do objeto (kg): "))
        velocidade_objeto = float(input("Digite a velocidade do objeto (m/s): "))
        momento_linear = massa_objeto * velocidade_objeto
        print(f"O momento linear é {momento_linear:.2f} kg m/s")




    elif Resposta_3 == 15:
        forca_aplicada = float(input("Digite a força aplicada (N): "))
        distancia_forca_centro = float(input("Digite a distância da força ao centro de rotação (metros): "))
        torque = forca_aplicada * distancia_forca_centro
        print(f"O torque é {torque:.2f} N m")




    elif Resposta_3 == 1:
        comprimento_onda = float(input("Digite o comprimento de onda (metros): "))
        frequencia_onda = float(input("Digite a frequência de onda (Hertz): "))
        velocidade_onda = comprimento_onda * frequencia_onda
        print(f"A velocidade da onda é {velocidade_onda:.2f} m/s")



    elif Resposta_3 == 1:
        velocidade_onda = float(input("Digite a velocidade da onda (m/s): "))
        frequencia_onda = float(input("Digite a frequência de onda (Hertz): "))
        comprimento_onda = velocidade_onda / frequencia_onda
        print(f"O comprimento da onda é {comprimento_onda:.2f} metros")




    elif Resposta_3 == 16:
        velocidade_onda = float(input("Digite a velocidade da onda (m/s): "))
        comprimento_onda = float(input("Digite o comprimento de onda (metros): "))
        frequencia_onda = velocidade_onda / comprimento_onda
        print(f"A frequência da onda é {frequencia_onda:.2f} Hertz")



    elif Resposta_3 == 17:
        tensao_eletrica = float(input("Digite a tensão elétrica (Volts): "))
        resistencia = float(input("Digite a resistência (Ohms): "))
        corrente_eletrica = tensao_eletrica / resistencia
        print(f"A corrente elétrica é {corrente_eletrica:.2f} Amperes")


    elif Resposta_3 == 18:
        corrente_eletrica = float(input("Digite a corrente elétrica (Amperes): "))
        resistencia = float(input("Digite a resistência (Ohms): "))
        tensao_eletrica = corrente_eletrica * resistencia
        print(f"A tensão elétrica é {tensao_eletrica:.2f} Volts")


elif Resposta == 7:
    Resposta_4 = int(input("Quantos lados tem a figura"))
    
    if Resposta_4 > 0:
        soma = int((Resposta_4 - 2) * 180)
        interno = int(((Resposta_4 - 2) * 180)/Resposta_4)




elif Resposta == 8:
    Resposta_5 = int(input("Quantas faces tem a base do solido"))
    if Resposta_5 == 3:
        lado1 = int(input("Qual a medida dos tres lados: "))
        lado2 = int(input())
        lado3 = int(input())
        semi = lado1 + lado2 + lado3
        area = semi * (semi - lado1) * (semi - lado2) * (semi - lado3)
        area = math.sqrt(area)
        area = area * 4


    if Resposta_5 == 4:
        lado1 = int(input("Digite o lado"))
        lado2 = int(input())
        area = lado1 * lado2 * 6




    if Resposta_5 == 5:
        print("Em caso de ser regular")
        lado1 = int(input("Digite o lado"))
        area = (pow(lado1, 2) * math.sqrt(3))/4
        area = area * 5






    if Resposta_5 == 6:
        print("Em caso de ser regular")
        lado1 = int(input("Digite o lado"))
        area = (pow(lado1, 2) * math.sqrt(3))/4
        area = area * 6





    if Resposta_5 == 7:
        print("Em caso de ser regular")
        lado1 = int(input("Digite o lado"))
        area = (pow(lado1, 2) * math.sqrt(3))/4
        area = area * 7
    
        
elif Resposta == 9:
    Resposta6 = int(input("Digite o numero correspondente: 1-Cubo 2-Piramide 3-Cilindro 4-Esfera 5-Outros tipos"))
    if Resposta6 == 1:
        lado = int(input("Digite o lado do cubo: "))
        volume = pow(lado, 3)


    elif Resposta6 == 2:
        lado1 = int(input("Qual a medida dos tres lados: "))
        lado2 = int(input())
        lado3 = int(input())
        semi = lado1 + lado2 + lado3
        area = semi * (semi - lado1) * (semi - lado2) * (semi - lado3)
        area = math.sqrt(area)
        altura = int(input("Qual a altura:"))
        volume = (area * altura)/3


    elif Resposta6 == 3:
        raio = int(input("Qual o  raio: "))
        altura = int(input("Qual a altura:"))
        volume = math.pi * pow(raio,2) * altura


    elif Resposta6 == 4:
        raio = int(input("Qual o  raio: "))
        volume = math.pi * pow(raio,3) * (4/3)
    
    elif Resposta == 5:
        raio = int(input("Qual o  raio: "))
        altura = int(input("Qual a altura:"))
        volume = (math.pi * pow(raio,2) * altura)/3

elif Resposta == 10:
    
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

  

elif Resposta == 11:
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




elif Resposta == 12:

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

    


