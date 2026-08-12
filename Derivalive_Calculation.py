import sympy as sp

#Variável simbólicas
x = sp.symbols("x")
print("="*50)
print(" CALCULADORA DE DERIVADAS ")
print("="*50)

#Grau da função
grau = int(input("\nDigite o grau do polinômio: "))

#Montagem da função
funcao = 0
print("\nDigite os coeficientes: ")
for expoente in range(grau, -1, -1):
    coeficiente = float(input(f"Coeficiente de x^{expoente}: "))
    funcao += coeficiente * x**expoente

#Calcula a derivada
derivada = sp.diff(funcao, x)

#Exibe os resultados
print("\n==================")
print("\n FUNÇÃO INFORMADA")
print("\n==================")
sp.pprint(funcao)
print("\n========")
print("\nDERIVADA")
print("\n========")
sp.pprint(derivada)

#Calculo para um valor específico de x
valor_x = float(input("\nDigite o valor de x: "))
resultado_funcao = funcao.subs(x, valor_x)
resultado_derivada = derivada.subs(x, valor_x)
print("\n=============================")
print(f"RESULTADOS PARA x = {valor_x}")
print("\n=============================")
print(f"f({valor_x}) = {resultado_funcao:.2f}")
print(f"f'({valor_x}) = {resultado_derivada:.2f}")
