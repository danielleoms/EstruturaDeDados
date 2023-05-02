# 13) Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até
# N em ordem decrescente.

def recursive_countup_recursive(start: int, finish: int) -> int:
    print(start, end=" ")
    if start <= finish:
        return start
    return recursive_countup_recursive((start - 1), finish)


if __name__ == "__main__":
    n = int(input("Digite um número: "))
    recursive_countup_recursive(n, 0)
