# 2. Crie uma função de busca em que o usuário insere um valor (inteiro) e o programa retorna a sua posição na fila.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Fila:
    def __init__(self):
        self.head = None # inicializa a fila com a cabeça apontando para None
        self.tail = None # inicializa a fila com a cauda apontando para None
        self.size = 0    # inicializa o tamanho da fila como 0
        
    def push(self, data):
        novo_no = Node(data)  # cria um novo nó com o valor passado como parâmetro
        if self.head is None: # caso a fila esteja vazia, o novo nó se torna a cabeça e a cauda da fila
            self.head = novo_no
            self.tail = novo_no
        else:
            self.tail.next = novo_no # adiciona o novo nó no final da fila
            self.tail = novo_no      # atualiza a cauda da fila
        self.size += 1 # incrementa o tamanho da fila
            
    def pop(self):
        if self.head is None: # caso a fila esteja vazia, retorna None
            return None
        else:
            no_removido = self.head # salva o nó que será removido da fila
            self.head = no_removido.next # atualiza a cabeça da fila para o próximo nó
            no_removido.next = None     # remove a referência para o próximo nó do nó removido
            self.size -= 1 # decrementa o tamanho da fila
            return no_removido.data # retorna o valor do nó removido
        
    def busca(self, valor):
        posicao = 1     # inicializa a posição como 1
        no_atual = self.head  # começa a busca a partir da cabeça da fila
        while no_atual is not None:
            if no_atual.data == valor: # caso encontre o valor na fila, retorna a posição
                return posicao
            posicao += 1       # incrementa a posição
            no_atual = no_atual.next # atualiza o nó atual
        return None # caso o valor não seja encontrado, retorna None
