import os
from pathlib import Path

import psycopg2


def carregar_env_local():
    caminho_env = Path(".env")

    if not caminho_env.exists():
        return

    for linha in caminho_env.read_text().splitlines():
        linha = linha.strip()

        if not linha or linha.startswith("#") or "=" not in linha:
            continue

        chave, valor = linha.split("=", 1)
        os.environ.setdefault(chave.strip(), valor.strip().strip('"').strip("'"))


class BancoDeDados:
    def __init__(self):
        carregar_env_local()

        senha = os.getenv("DB_PASSWORD")

        if not senha:
            raise RuntimeError(
                "Configure a variavel de ambiente DB_PASSWORD antes de iniciar o sistema."
            )

        self.conexao = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "sistema_ponto"),
            user=os.getenv("DB_USER", "postgres"),
            password=senha,
            port=os.getenv("DB_PORT", "5432"),
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
