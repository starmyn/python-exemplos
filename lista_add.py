alunos = ["Ivone"]
alunos.append("Tábata")
while True:
    nome = input ("Digite o nome do aluno" )
    alunos.append(nome)
    resposta = input("Deseja adicionar mais um aluno? S/N): ")
    if resposta.upper() == "N":
        break 
print(f"Alunos cadastrados:{alunos}")