import sympy as sp

x = sp.symbols("x")

grau = int(input("Grau do polinomio: "))

funcao = 0

for expoente in range(grau, -1, -1):
    coef = float(input(f"Coeficiente de x^{expoente}: "))
    funcao += coef * x**expoente

print("Funcao: ")
sp.pprint(funcao)

a = float(input("\nLimite inferior: "))
b = float(input("\nLimite superior: "))

resultado = sp.integrate(funcao, (x, a, b))

print("\nIntegral definida: ")
sp.pprint(resultado)

print("\nValor decimal: ", float(resultado))