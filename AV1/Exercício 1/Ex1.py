
#Escreva um Método em python para remover elementos repetidos de uma pilha

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def remove_duplicates(self):
        seen_items = set()
        result = []
        while not self.is_empty():
            item = self.pop()
            if item not in seen_items:
                result.append(item)
                seen_items.add(item)
        result.reverse()
        self.items = result


s = Stack()
s.push(3)
s.push(3)
s.push(3)
s.push(6)
s.push(6)
s.push(9)
s.push(10)
s.push(12)

print("Pilha original:", s.items)
s.remove_duplicates()
print("Pilha sem duplicatas:", s.items)

