# 15) Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até
# N em ordem decrescente.

def print_even_numbers_reverse(start: int, end: int) -> None:
    if start < end:
        return
    print(start, end=" ")
    print_even_numbers_reverse(start - 2, end)

n = int(input("Digite um número par: "))
print_even_numbers_reverse(n, 0)
