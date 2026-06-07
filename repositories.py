from datetime import datetime
from models import Funcionario, RegistroPonto


# lembrar de conferir o fluxo
class RepositorioFuncionario:
    def __init__(self, banco):
        self.banco = banco

    def buscar_por_matricula(self, matricula):
        sql = """
            SELECT id, matricula, nome, ativo
            FROM funcionarios
            WHERE matricula = %s;
        """

        resultado = self.banco.consultar_um(sql, (matricula,))

        if resultado is None:
            return None

        return Funcionario(
            id=resultado[0],
            matricula=resultado[1],
            nome=resultado[2],
            ativo=resultado[3],
        )

    def cadastrar(self, matricula, nome):
        sql = """
            INSERT INTO funcionarios (matricula, nome)
            VALUES (%s, %s);
        """

        self.banco.executar(sql, (matricula, nome))


class RepositorioPonto:
    def __init__(self, banco):
        self.banco = banco

    # Busca pendencia
    def buscar_registro_aberto(self, funcionario_id):
        sql = """
            SELECT id, funcionario_id, chegada, saida
            FROM registros_ponto
            WHERE funcionario_id = %s
              AND saida IS NULL
            ORDER BY chegada DESC
            LIMIT 1;
        """

        resultado = self.banco.consultar_um(sql, (funcionario_id,))

        if resultado is None:
            return None

        return RegistroPonto(
            id=resultado[0],
            funcionario_id=resultado[1],
            chegada=resultado[2],
            saida=resultado[3],
        )

    # Registra chegada
    def registrar_chegada(self, funcionario_id):
        sql = """
            INSERT INTO registros_ponto (funcionario_id, chegada)
            VALUES (%s, %s);
        """

        self.banco.executar(sql, (funcionario_id, datetime.now()))

    # Registra saida
    def registrar_saida(self, registro_id):
        sql = """
            UPDATE registros_ponto
            SET saida = %s
            WHERE id = %s;
        """

        self.banco.executar(sql, (datetime.now(), registro_id))

    # Historico
    def listar_todos(self):
        sql = """
            SELECT
                rp.id,
                f.nome,
                f.matricula,
                rp.chegada,
                rp.saida
            FROM registros_ponto rp
            INNER JOIN funcionarios f
                ON rp.funcionario_id = f.id
            ORDER BY rp.chegada DESC;
        """

        return self.banco.consultar_todos(sql)

    def listar_presentes(self):
        sql = """
            SELECT
                rp.id,
                f.nome,
                f.matricula,
                rp.chegada
            FROM registros_ponto rp
            INNER JOIN funcionarios f
                ON rp.funcionario_id = f.id
            WHERE rp.saida IS NULL
            ORDER BY rp.chegada DESC;
        """

        return self.banco.consultar_todos(sql)
