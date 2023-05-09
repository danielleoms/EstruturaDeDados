
# Escreva um método em python para remover elementos cujos
# valores estão em um range específico em uma lista encadeada

class Nodo:
    def __init__(self, dado=None, proximo=None):
        self.dado = dado
        self.proximo = proximo


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def __str__(self):
        resultado = ""
        nodo_atual = self.cabeca
        while nodo_atual:
            resultado += str(nodo_atual.dado) + " -> "
            nodo_atual = nodo_atual.proximo
        resultado += "None"
        return resultado

    def insere_no_inicio(self, valor):
        novo_nodo = Nodo(valor, self.cabeca)
        self.cabeca = novo_nodo

    def remove(self, valor):
        assert self.cabeca, "Não foi possivel remover valor de lista vazia."

        if self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
        else:
            anterior = None
            corrente = self.cabeca
            while corrente and corrente.dado != valor:
                anterior = corrente
                corrente = corrente.proximo
            if corrente:
                anterior.proximo = corrente.proximo
            else:
                anterior.proximo = None

    def remove_range(self, inicio, fim):
        assert self.cabeca, "Não foi possivel remover valores de lista vazia."

        nodo_atual = self.cabeca
        while nodo_atual:
            if inicio <= nodo_atual.dado <= fim:
                self.remove(nodo_atual.dado)
            nodo_atual = nodo_atual.proximo


lista = ListaEncadeada()

lista.insere_no_inicio(3)
lista.insere_no_inicio(5)
lista.insere_no_inicio(6)
lista.insere_no_inicio(8)
lista.insere_no_inicio(10)
lista.insere_no_inicio(12)
print("Lista:", lista)

inicio = 2
fim = 7
lista.remove_range(inicio, fim)
print("Lista após a remoção:", lista)

#Relatório#
"""
- Foi adicionado  o método "remove_range" que recebeu os parâmetros "inicio" e "fim" que definem
o range de valores a serem removidos. Em seguida, foi percorrida a lista e verificado se o valor do nodo está dentro do range especificado.
Caso esteja, o método "remove" é utilizado para remover o valor da lista. Por fim, é impressa a lista após a remoção.
"""
