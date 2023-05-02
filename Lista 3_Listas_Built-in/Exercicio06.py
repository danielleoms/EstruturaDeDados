# 10) Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

alunos = 10
medias = []

for i in range(alunos):
    notas = []
    for j in range(4):
        while True:
            nota = float(input(f"Informe a nota {j + 1} do aluno {i+1}: "))
            if 0 <= nota <= 10:
                break
            print("Nota inválida! A nota deve estar entre 0 e 10.")
        notas.append(nota)
    
    media = sum(notas)/len(notas)
    medias.append(media)

print(f"Médias dos alunos: {medias}")

aprovados = 0
for media in medias:
    if media >= 7.0:
        aprovados += 1

print(f"Quantidade de alunos aprovados: {aprovados}")
