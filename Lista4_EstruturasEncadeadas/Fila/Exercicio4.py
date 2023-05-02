'''4) . Construa um programa utilizando uma pilha que resolva o seguinte problema: 

Armazene as placas dos carros (apenas os números) que estão estacionados numa rua sem saída estreita. 
Dado uma placa verifique se o carro está estacionado na rua. 
Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair.'''

class Estacionamento:
    def __init__(self):
        self.pilha = []
    
    def estacionar(self, placa):
        self.pilha.append(placa)
    
    def retirar(self, placa):
        posicao = None
        qtd_retiradas = 0
        # Procura a posição da placa na pilha e conta quantas retiradas serão necessárias
        for i in range(len(self.pilha)):
            if self.pilha[i] == placa:
                posicao = i
                qtd_retiradas = len(self.pilha) - i - 1
                break
        # Se a placa não está na pilha, retorna None
        if posicao is None:
            return None
        # Retira os carros da pilha até chegar na posição da placa
        for i in range(qtd_retiradas):
            self.pilha.pop()
        return qtd_retiradas

# Exemplo de uso
estacionamento = Estacionamento()
estacionamento.estacionar("ABC1234")
estacionamento.estacionar("DEF5678")
estacionamento.estacionar("GHI9101")
estacionamento.estacionar("JKL2345")
placa = "GHI9101"
qtd_retiradas = estacionamento.retirar(placa)
if qtd_retiradas is not None:
    print(f"O carro com placa {placa} pode sair após {qtd_retiradas} retiradas.")
else:
    print(f"O carro com placa {placa} não está estacionado na rua.")
