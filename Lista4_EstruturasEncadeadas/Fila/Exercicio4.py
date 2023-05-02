''' 4) Escreva uma função que inverta a ordem dos elementos da fila.  Por exemplo:

[1] [4] [5] [2] → [2] [5] [4] [1]'''

def inverte_fila(fila):
    pilha_aux = []

    # remove todos os elementos da fila e insere na pilha auxiliar
    while len(fila) > 0:
        pilha_aux.append(fila.pop(0))

    # remove todos os elementos da pilha auxiliar e insere de volta na fila
    while len(pilha_aux) > 0:
        fila.append(pilha_aux.pop())

    return fila
  
fila = [1, 4, 5, 2]
print("Fila antes da inversão: ", fila)

fila = inverte_fila(fila)
print("Fila após a inversão: ", fila)
