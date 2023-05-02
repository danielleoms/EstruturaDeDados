# Define a classe Node que representa um nó na lista encadeada.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Define a função remove_duplicates que recebe a cabeça da lista encadeada e remove todos os elementos duplicados.
def remove_duplicates(head):
    current = head # Define o nó atual como a cabeça da lista.
    while current: # Enquanto existir um nó atual.
        if current.next and current.val == current.next.val: # Se houver um próximo nó e seu valor for igual ao nó atual.
            current.next = current.next.next # Remove o próximo nó duplicado.
        else:
            current = current.next # Move o ponteiro atual para o próximo nó.
    return head # Retorna a cabeça da lista sem os elementos duplicados.
