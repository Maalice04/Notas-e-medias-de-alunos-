#leia dez numeros inteiros 
numeros = []
for i in range(10): 
    Numero= int(input(f"Digite o {i + 1}° número inteiro:"))
    numeros. append(Numero) 

#exibindo numeros pares 
print("\nNúmeros pares digitados:") 
for numero in numeros: 
    if numero % 2 == 0: 
        print(numero) 