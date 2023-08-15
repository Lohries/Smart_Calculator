import sympy as sp

while True:
    resposta = input("Quer calcular a derivada? (Sim/Nao): ")
    if resposta == "Sim":
        expression = input("Entre a funcao: ")
        variable = input("Entre a variavel: ")
        
        x = sp.Symbol(variable)
        f = sp.sympify(expression)
        derivative = sp.diff(f, x)

        print("A derivada de", expression, "em relacao", variable, "é:")
        print(derivative)
        
    elif resposta == "Nao":
        print("Até Mais")
        break
