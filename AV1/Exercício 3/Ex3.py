# Escreva uma função em python para somar todos os valores de uma fila recursiva


def soma_fila_recursiva(fila):
    if len(fila) == 0:  # caso base: fila vazia
        return 0
    else:
        primeiro = fila[0]
        resto = fila[1:]
        return primeiro + soma_fila_recursiva(resto)

fila = [1, 2, 3, 4, 5]
resultado = soma_fila_recursiva(fila)
print(resultado)  # output: 15

