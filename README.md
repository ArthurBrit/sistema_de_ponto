````md
# Sistema de Ponto

Projeto simples em Python para registrar entrada e saída de funcionários usando PostgreSQL.

## Requisitos

- Python 3
- PostgreSQL
- psycopg2

## Instalação

```bash
pip install psycopg2
````

Ou usando ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install psycopg2
```

## Configuração

Crie um arquivo `.env` na raiz do projeto usando o `.env.example` como base:

```env
DB_HOST=localhost
DB_NAME=sistema_ponto
DB_USER=postgres
DB_PASSWORD=sua_senha_real
DB_PORT=5432
```

O arquivo `.env` não deve ser enviado para o GitHub, pois contém dados sensíveis.

Também dá para configurar a senha pelo PowerShell:

```powershell
$env:DB_PASSWORD="sua_senha_real"
```

## Banco de dados

Crie as tabelas abaixo no PostgreSQL:

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

## Como rodar

Depois de configurar o banco, execute:

```bash
python main.py
```

## Observações

* Não coloque senha direto no código.
* Não envie o arquivo `.env` para o repositório.
* Se uma senha real já foi enviada, troque ela no PostgreSQL.

```
```
