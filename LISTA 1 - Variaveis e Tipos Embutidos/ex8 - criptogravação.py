#criptografar
dado = input("digite o dado desejado:")

resultado =""
bolodez = ""

for c in dado:
    novo = (int(c) + 7) %10
    resultado += str(novo)
 
cripto = resultado[2] + resultado[3] +resultado[0]+ resultado[1]

print("Criptografado:",cripto)

#descriptografar
dadocripto = input("digite um dado de quatro digitos criptografado:")

desfeito = dadocripto[2] + dadocripto[3] + dadocripto[0] + dadocripto[1]

resultado= ""

for c in desfeito:
    original = (int(c) - 7) % 10
    resultado += str(original)

print("Original:",resultado)
