#Danielle Moreno e Lucas Santini
# Escreva uma função em python para somar todos os valores de uma fila recursiva

from queue import Queue

def somatorioFila(fila: Queue) -> int:
    soma = 0
    while not fila.empty():
        elemento = fila.get()
        if isinstance(elemento, Queue):
            soma += somatorioFila(elemento)
        else:
            soma += elemento
    return soma

if __name__ == "__main__":
    filaX = Queue()
    filaX.put(25)
    filaX.put(Queue())
    filaX.put(4)
    filaX.put(Queue())
    filaX.put(Queue())
    filaX.put(555)
    print(f"A soma dos elementos da fila é {somatorioFila(filaX)}")
