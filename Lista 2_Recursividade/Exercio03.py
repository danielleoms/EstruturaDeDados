# 3) Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 - 321


def inverte_numero_lista(lista: list, inicio: int, fim: int) -> list:
    if inicio >= fim:
        return
    temp = lista[inicio]
    lista[inicio] = lista[fim]
    lista[fim] = temp
    inverte_numero_lista(lista, inicio + 1, fim - 1)


if __name__ == "__main__":
    numero = 123
    lista = list(str(numero))
    inverte_numero_lista(lista, 0, len(lista) - 1)
    numero_invertido = int(''.join(lista))
    print(numero_invertido)
