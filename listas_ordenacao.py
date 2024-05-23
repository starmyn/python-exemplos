import random
alunos=['Joao','Maria','Pedro','Ana','Lucas','Mariana']
print(f"Lista: {alunos}")
random.shuffle(alunos)
print("Lista embaralhada: {alunos}")
alunos.sort()
print(f"lista crescente:{alunos}")
alunos.sort(reverse=True)
print(f"Lista decrescente: {alunos}")
