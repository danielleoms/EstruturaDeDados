# 3)  Crie uma função que percorre e imprime todos os elementos da fila.

def imprime_fila(fila):
    # Verifica se a fila está vazia
    if fila.vazia():
        print("Fila vazia")
    else:
        # Inicia pelo nó da frente da fila
        no_atual = fila.frente.proximo
        while no_atual is not None:
            # Imprime o valor contido no nó atual
            print(no_atual.valor)
            # Atualiza o nó atual para o próximo nó da fila
            no_atual = no_atual.proximo
