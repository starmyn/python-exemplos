import random
alunos=['Joao','Maria','Pedro','Ana','Lucas','Mariana']
print(f"Lista: {alunos}")
random.shuffle(alunos)
print("Lista embaralhada: {alunos}")
aluno_sorteado = random.choice(alunos)
print(f"Aluno sorteado: {aluno_sorteado}")