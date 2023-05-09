# Escreva uma função em python para somar todos os valores de uma fila recursiva

class Nodo:
    """Esta classe representa um nó em uma lista encadeada"""

    def __init__(self, dado=0, proximo_no=None):
        self.dado = dado
        self.proximo = proximo_no

    def __repr__(self):
        return f"{self.dado} -> {self.proximo}"


class Fila:
    """Essa classe representa uma fila usando uma estrutura de lista encadeada"""

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return f"[{self.primeiro}]"

    def push(self, novo_dado):
        """Insere um elemento no final da fila"""

        novo_no = Nodo(novo_dado)

        if self.primeiro is None:
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no

    def pop(self):
        """Remove o primeiro elemento da fila"""

        assert self.primeiro is not None, "Impossível remover elemento de uma fila vazia"

        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None


def soma_lista(corrente):
    if not corrente:
        return 0
    return corrente.dado + soma_lista(corrente.proximo)


fila = Fila()
for i in range(15):
    fila.push(i)
print(f"Fila formada: {fila}")
soma = soma_lista(fila.primeiro)
print(f"Soma dos elementos da fila: {soma}")

#Relatório#
"""
- O código foi refeito com o objetivo de seguir as regras da recursividade
"""
