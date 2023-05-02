''' 5) Implemente uma função chamada TPilha, que receba um vetor de inteiros com 15 elementos. Para cada um deles, como segue: 

Se o número for par, insira-o na pilha; 
Se o número lido for ímpar, retire um número da pilha; 
Ao final, esvazie a pilha imprimindo os elementos.'''

def TPilha(vetor):
    pilha = []
    for numero in vetor:
        if numero % 2 == 0:
            pilha.append(numero)
        else:
            if pilha:
                pilha.pop()
    while pilha:
        print(pilha.pop())
