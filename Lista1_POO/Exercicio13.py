# Implemente a classe funcionário

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def retornar_nome(self):
        return self.nome

    def retornar_salario(self):
        return self.salario


funcionario1 = Funcionario('Dani', 2400)
print(f"O nome do funcionário 1 é {funcionario1.retornar_nome()}")
print(f"O salário do funcionário 1 é R${funcionario1.retornar_salario():.2f}")
