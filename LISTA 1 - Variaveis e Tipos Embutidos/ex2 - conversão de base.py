numero = input("digite um numero:\n")
base = int(input("digite uma base(8,10 ou 16)\n"))

valor = int(numero, base)

print("Valor em decimal: ", valor)
print("Valor em hexadecimal: ", hex(valor))
print("Valor em octal:", oct(valor))
