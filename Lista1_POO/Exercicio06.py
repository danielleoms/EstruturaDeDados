# Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV:
    def __init__(self, canal=0, volume=0):
        if 0 < canal < 200:
            self.canal = canal
        if 0 < volume < 100:
            self.volume = volume

    def trocar_canal(self, novo_canal):
        if 0 < novo_canal < 200:
            self.canal = novo_canal

    def aumentar_volume(self, novo_volume):
        if novo_volume > self.volume and 0 < novo_volume < 100:
            self.volume = novo_volume

    def diminuir_volume(self, novo_volume):
        if novo_volume < self.volume and 0 < novo_volume < 100:
            self.volume = novo_volume
