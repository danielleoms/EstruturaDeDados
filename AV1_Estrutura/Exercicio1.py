#Danielle Moreno e Lucas Santini
#Escreva um Método em python para remover elementos repetidos de uma pilha

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_duplicates(head):
    current = head
    while current is not None and current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return head


head = Node(3)
head.next = Node(3)
head.next.next = Node(3)
head.next.next.next = Node(6)
head.next.next.next.next = Node(6)
head.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next = Node(10)
head.next.next.next.next.next.next.next = Node(12)


current = head
while current is not None:
    print(current.value, end=" → ")
    current = current.next
print("None")


head = remove_duplicates(head)


current = head
while current is not None:
    print(current.value, end=" → ")
    current = current.next
print("None")

