class Funcionario:
    def __init__(self, id, matricula, nome, ativo=True):
        self.id = id
        self.matricula = matricula
        self.nome = nome
        self.ativo = ativo


class RegistroPonto:
    def __init__(self, id, funcionario_id, chegada, saida=None):
        self.id = id
        self.funcionario_id = funcionario_id
        self.chegada = chegada
        self.saida = saida

    def esta_aberto(self):
        return self.saida is None
