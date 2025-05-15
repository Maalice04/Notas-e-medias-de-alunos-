#coletar dados dos 5 alunos 
alunos = []

# Coletando dados de 5 alunos
for i in range(3):
    
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2

#exibiçao e soma das informaçoes em lista (linha da MATRIZ)
alunos.append([nome, nota1, nota2, media])

print("\n---Resultado Final---")
for aluno in alunos:
    print(f"{aluno[0]} - Nota1: {aluno[1]} | Nota2: {aluno[2]} | Média: {aluno[3]:.2f}")
   