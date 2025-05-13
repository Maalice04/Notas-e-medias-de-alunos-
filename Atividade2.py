#coletar dados dos 5 alunos 
alunos = []

# Coletando dados de 5 alunos
for i in range(5):
    print(f"\nAluno {i + 1}:")
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    media = (nota1 + nota2) / 2
#exibiçao e soma das informaçoes 
    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media": media
    }
    
    alunos.append(aluno)

# Exibindo os dados de todos os alunos
print("\n--- Dados dos Alunos ---")
for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Nota 1: {aluno['nota1']:.2f}")
    print(f"Nota 2: {aluno['nota2']:.2f}")
    print(f"Média: {aluno['media']:.2f}")
    print("-" * 20)
