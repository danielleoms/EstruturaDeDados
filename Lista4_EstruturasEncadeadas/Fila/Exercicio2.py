# 2) Utilizando uma pilha resolver o exercício a seguir: Dada uma sequência contendo N (N >0) números reais, imprimi-la na ordem inversa.

def imprime_inverso(seq):
    pilha = []
    # Empilha todos os elementos da sequência
    for elemento in seq:
        pilha.append(elemento)
    # Desempilha os elementos e imprime na ordem inversa
    while len(pilha) > 0:
        print(pilha.pop())


# Programa principal
N = int(input("Digite o número de elementos da sequência: "))
seq = []
for i in range(N):
    elemento = float(input("Digite o {}º elemento: ".format(i + 1)))
    seq.append(elemento)

imprime_inverso(seq)
