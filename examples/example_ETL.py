from my_data_lib.factory import get_data_handler

# 1. Ler dados de um arquivo CSV
csv_handler = get_data_handler("csv", path="data/clientes.csv")
df_csv = csv_handler.read()
print("Dados lidos do CSV:")
print(df_csv.head())

# 2. Salvar esses dados em uma tabela do Postgres
postgres_handler = get_data_handler(
    "postgres",
    host="localhost",
    port=5432,
    database="meu_banco",
    user="usuario",
    password="senha"
)
postgres_handler.write(df_csv, table_name="clientes")

# 3. Ler os dados do Postgres
df_pg = postgres_handler.read("SELECT * FROM clientes WHERE status = 'ativo';")
print("Dados lidos do Postgres:")
print(df_pg.head())

# 4. Salvar os dados ativos no MongoDB
mongo_handler = get_data_handler(
    "mongodb",
    uri="mongodb://localhost:27017",
    database="meubanco",
    collection="clientes_ativos"
)
mongo_handler.write(df_pg)

print("Fluxo completo executado com sucesso!")