import psycopg2


class BancoDeDados:
    def __init__(self):
        self.conexao = psycopg2.connect(
            host="localhost",
            database="sistema_ponto",
            user="postgres",
            password="postgres",
            port="5432",
        )

    def executar(self, sql, parametros=None):
        with self.conexao.cursor() as cursor:
            cursor.execute(sql, parametros)
            self.conexao.commit()

    def consultar_um(self, sql, parametros=None):
        with self.conexao.cursor() as cursor:
            cursor.execute(sql, parametros)
            return cursor.fetchone()

    def consultar_todos(self, sql, parametros=None):
        with self.conexao.cursor() as cursor:
            cursor.execute(sql, parametros)
            return cursor.fetchall()

    def fechar(self):
        self.conexao.close()
