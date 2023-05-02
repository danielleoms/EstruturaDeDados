# 1) Escrever uma função que receba como parâmetro uma pilha. A função deve retornar o maior elemento da pilha.

def maior_elemento(pilha):
    maior = None
    # Percorre toda a pilha
    while not pilha.esta_vazia():
        # Obtém o valor do topo da pilha
        topo = pilha.desempilha()
        # Verifica se é o maior valor encontrado até agora
        if maior is None or topo > maior:
            maior = topo
    # Retorna o maior valor encontrado
    return maior
