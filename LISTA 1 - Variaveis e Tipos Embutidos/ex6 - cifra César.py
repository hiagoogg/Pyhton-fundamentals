texto = input("digite um texto:\n")
desloc = int(input("digite o deslocamento:\n"))

resultado = ""

for c in texto:
    if c == " ":
        resultado += " "
    elif "a" <= c <= "z":
        novo = (ord(c) - ord("a") + desloc) %26 + ord("a")
        resultado += chr(novo)
    elif "A" <= c <="Z":
        novo = (ord(c) - ord("A") + desloc) %26 + ord("A")
        resultado += chr(novo)
    else:
        resultado += c

print("Texto cifrado:", resultado)
    
