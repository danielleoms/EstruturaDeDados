#1) Implemente a função remove utilizando a função busca. 

def remove(lista, valor):
    if lista is None:  # caso a lista esteja vazia
        return lista
    
    if lista.dado == valor:  # caso o elemento a ser removido seja o primeiro
        lista = lista.prox
        return lista
    
    anterior = busca(lista, valor)  # busca o elemento anterior ao que será removido
    if anterior is None:  # caso o valor não esteja na lista
        return lista
    
    elemento = anterior.prox
    anterior.prox = elemento.prox  # atualiza o ponteiro do elemento anterior
    del elemento  # exclui o elemento
    return lista
