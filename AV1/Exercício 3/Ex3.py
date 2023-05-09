# Escreva uma função em Python para somar todos os valores de uma fila de forma recursiva

class Nodo:
    """ Esta classe representa um nodo em uma encadeada"""

    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return "%s -> %s" % (self.dado, self.proximo)


class Fila:
    """ Esssa classe representa uma fila usando uma estrutura encadeada"""

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def push(self, novo_dado):
        """Inseri um elemento no final da fila"""

        novo_nodo = Nodo(novo_dado)

        if self.primeiro is None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def pop(self):
        """Remove o primeiro elemento da fila"""

        assert self.primeiro is not None, "Impossível remover elemento de fila vazia"

        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None


def somaLista(fila: Fila) -> int:
    if fila.primeiro is None:
        return 0
    else:
        soma = fila.primeiro.dado
        fila.pop()
        return soma + somaLista(fila)
