frase = input("Digite uma frase:")

qvogal = 0

for c in frase:
    if c in "aeiou":
        qvogal+= 1
    elif c in "AEIOU":
        qvogal+= 1

print("quantidade de vogais:", qvogal)
        
