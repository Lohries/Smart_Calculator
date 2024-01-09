from advance_library import *

# Programa principal
while True:
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Áreas de Figuras Planas")
    print("6 - Fórmulas Físicas")
    print("7 - Ângulos")
    print("8 - Áreas de Sólidos Geométricos")
    print("9 - Volume")
    print("10 - Derivadas")
    print("11 - Integrais")
    print("12 - Calculadora Gráfica")
    print("0 - Sair")

    choice = int(input("Digite o número da operação desejada: "))

    if choice == 0:
        break

    if choice == 1:
        calculate_sum()
    elif choice == 2:
        calculate_difference()
    elif choice == 3:
        calculate_product()
    elif choice == 4:
        calculate_quotient()
    elif choice == 5:
        calculate_area()
    elif choice == 6:
        # Adicione a opção para cálculos físicos
        print("Escolha a operação de física:")
        print("1 - Peso")
        print("2 - Empuxo")
        print("3 - Força de Atrito")
        print("4 - Força Resultante")
        # Adicione mais opções conforme necessário...

        physics_choice = int(input("Digite o número da operação desejada: "))
        if physics_choice == 1:
            calculate_weight()
        elif physics_choice == 2:
            calculate_buoyancy()
        elif physics_choice == 3:
            calculate_friction_force()
        elif physics_choice == 4:
            calculate_resultant_force()
        # Adicione mais casos conforme necessário...
    elif choice == 7:
        calculate_angles()
    elif choice == 8:
        # Adicione a opção para cálculos de áreas de sólidos geométricos
        print("Escolha o sólido geométrico:")
        print("1 - Tetraedro (Triângulo Equilátero)")
        print("2 - Cubo")
        print("3 - Cilindro")
        # Adicione mais opções conforme necessário...

        solid_choice = int(input("Digite o número do sólido desejado: "))
        if solid_choice == 1:
            # Adicione a lógica para calcular a área do tetraedro
            pass
        elif solid_choice == 2:
            # Adicione a lógica para calcular a área do cubo
            pass
        elif solid_choice == 3:
            # Adicione a lógica para calcular a área do cilindro
            pass
        # Adicione mais casos conforme necessário...
    elif choice == 9:
        calculate_volume()
    elif choice == 10:
        calculate_derivative()
    elif choice == 11:
        calculate_integral()
    elif choice == 12:
        graph()
    else:
        print("Escolha inválida. Tente novamente.")
