# 3) Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais. Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.

def pilhas_sao_iguais(pilha1, pilha2):
    # Se as pilhas têm tamanhos diferentes, elas não são iguais
    if len(pilha1) != len(pilha2):
        return False
    # Verifica se cada elemento das pilhas é igual, na mesma ordem
    for i in range(len(pilha1)):
        if pilha1[i] != pilha2[i]:
            return False
    # Se chegou aqui, as pilhas são iguais
    return True
