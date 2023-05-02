'''Escreva uma função chamada TPilha2 que recebe como parâmetro 2 pilhas (N e P) e um vetor de inteiros. Para cada um: 

se positivo, inserir na pilha P; 
se negativo, inserir na pilha N; 
se zero, retirar um elemento de cada pilha.'''

def TPilha2(N, P, vetor):
    for numero in vetor:
        if numero > 0:
            P.append(numero)
        elif numero < 0:
            N.append(numero)
        else:
            if N:
                N.pop()
            if P:
                P.pop()
