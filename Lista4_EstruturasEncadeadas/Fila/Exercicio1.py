'''1. Implemente uma fila dinâmica contendo todas as funcionalidades de uma fila padrão. Para isso, resolvar:
–Crie um nó padrão da fila.
–Crie uma função de inicialização da fila vazia
–Crie uma função push que cria e insere um novo nó para o final da fila.
–Crie uma função pop que remove o primeiro elemento da fila.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Fila:
    def __init__(self):
        self.front = None  # aponta para o primeiro elemento da fila
        self.rear = None   # aponta para o último elemento da fila
        
    def push(self, data):
        '''Insere um novo nó no final da fila.'''
        new_node = Node(data)  # cria um novo nó com o dado a ser inserido
        if self.front is None:  # caso a fila esteja vazia
            self.front = new_node  # o novo nó será o primeiro e último elemento da fila
            self.rear = new_node
        else:
            self.rear.next = new_node  # atualiza o ponteiro do último nó para o novo nó
            self.rear = new_node  # atualiza o ponteiro do último nó para o novo nó
            
    def pop(self):
        '''Remove o primeiro elemento da fila.'''
        if self.front is None:  # caso a fila esteja vazia, não há elementos a serem removidos
            return None
        else:
            removed_node = self.front  # armazena o nó a ser removido
            self.front = self.front.next  # atualiza o ponteiro do primeiro nó para o próximo nó
            if self.front is None:  # caso a fila tenha apenas um elemento, ao removê-lo, a fila ficará vazia
                self.rear = None
            return removed_node.data
