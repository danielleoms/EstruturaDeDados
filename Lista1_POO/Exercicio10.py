'''Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
    Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
        tipoCombustivel.
        valorLitro
        quantidadeCombustivel

    Possua no mínimo esses métodos:
        abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
        quantidade de litros que foi colocada no veículo

        abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível
        e mostra o valor a ser pago pelo cliente.

        alterarValor( ) – altera o valor do litro do combustível.

        alterarCombustivel( ) – altera o tipo do combustível.

        alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

        OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de
        combustível total na bomba. '''

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def alterar_valor(self, valor):
        self.valorLitro = valor

    def alterar_combustivel(self, combustivel):
        self.tipoCombustivel = combustivel

    def alterar_quantidade_combustivel(self, quant):
        self.quantidadeCombustivel = quant

    def abastercer_por_valor(self, valor):
        quant = valor/self.valorLitro
        self.quantidadeCombustivel += quant
        return quant

    def abastecer_por_litros(self, litros):
        self.quantidadeCombustivel += litros
        return litros/self.valorLitro
