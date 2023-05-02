# 3) Defina as funções inserção, remoção e busca como métodos da Classe Lista. 

# Método para inserir um novo nó na lista
def inserir(self, data):
    novo_node = Node(data)  # Criando um novo nó com o valor fornecido
    if self.head is None:  # Se a lista estiver vazia
        self.head = novo_node  # O novo nó se torna a cabeça da lista
    else:
        current = self.head  # Percorrendo a lista até o último nó
        while current.next:
            current = current.next
        current.next = novo_node  # O novo nó é adicionado ao final da lista

# Método para remover um nó da lista
def remover(self, data):
    if self.head is None:  # Se a lista estiver vazia
        return
    if self.head.data == data:  # Se o nó a ser removido for a cabeça da lista
        self.head = self.head.next  # A nova cabeça da lista é o próximo nó
    else:
        current = self.head  # Percorrendo a lista até encontrar o nó a ser removido
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # Removendo o nó da lista
                return
            current = current.next

# Método para buscar um valor na lista
def buscar(self, data):
    current = self.head  # Percorrendo a lista até encontrar o valor
    while current:
        if current.data == data:
            return True
        current = current.next
    return False  # Retornando False se o valor não for encontrado
