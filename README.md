# Sistema de Ponto

Sistema simples em Python para registrar chegada e saida de funcionarios usando PostgreSQL.

## Requisitos

- Python 3
- PostgreSQL
- Pacote `psycopg2`

## Instalacao

Instale a dependencia principal:

```bash
pip install psycopg2
```

Se preferir usar ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install psycopg2
```

## Configuracao do banco

Este projeto nao salva a senha do banco no codigo. Crie um arquivo `.env` local ou configure as variaveis de ambiente manualmente.

Use o arquivo `.env.example` como modelo:

```env
DB_HOST=localhost
DB_NAME=sistema_ponto
DB_USER=postgres
DB_PASSWORD=sua_senha_real
DB_PORT=5432
```

O arquivo `.env` esta no `.gitignore`, entao ele nao deve ser enviado para o Git.

No PowerShell, voce tambem pode configurar a senha assim antes de executar:

```powershell
$env:DB_PASSWORD="sua_senha_real"
```

As outras variaveis possuem valores padrao:

- `DB_HOST`: `localhost`
- `DB_NAME`: `sistema_ponto`
- `DB_USER`: `postgres`
- `DB_PORT`: `5432`

## Tabelas esperadas

O sistema espera as tabelas abaixo no PostgreSQL:

```sql
CREATE TABLE funcionarios (
    id SERIAL PRIMARY KEY,
    matricula VARCHAR(50) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    ativo BOOLEAN DEFAULT TRUE
);

CREATE TABLE registros_ponto (
    id SERIAL PRIMARY KEY,
    funcionario_id INTEGER NOT NULL REFERENCES funcionarios(id),
    chegada TIMESTAMP NOT NULL,
    saida TIMESTAMP
);
```

## Como executar

Configure `DB_PASSWORD` e execute:

```bash
python main.py
```

## Cuidados com credenciais

- Nunca coloque senha real em arquivos `.py`.
- Nunca versione o arquivo `.env`.
- Se uma senha ja foi enviada para um repositorio remoto, troque essa senha no PostgreSQL.
