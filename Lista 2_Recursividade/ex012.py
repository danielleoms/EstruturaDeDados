# 12) Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até
# N em ordem crescente.

def contagem_progressiva_recursiva(comeca_em: int, termina_em: int) -> int:
    print(comeca_em, end= " ")
    if comeca_em >= termina_em:
        return comeca_em
    return contagem_progressiva_recursiva((comeca_em + 1), termina_em)


if __name__ == "__main__":
    n = int(input("Digite um número: "))
    contagem_progressiva_recursiva(0, n)