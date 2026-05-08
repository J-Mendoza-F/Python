# CONTADOR DE VOCALES

texto=input("Escriba su texto: ")

vocales="aeiou"
cont=0

for letra in texto:
    if letra in vocales:
        cont+=1
        
print(f"Cantidad de vocales: {cont}")