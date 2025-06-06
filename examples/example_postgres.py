from my_data_lib.factory import get_data_handler

# Crie o handler usando a factory
handler = get_data_handler(
    "postgres",
    host="localhost",
    port=5432,
    database="meu_banco",
    user="usuario",
    password="senha"
)

# Leitura de dados
df = handler.read("SELECT * FROM clientes WHERE status = 'ativo';")
print(df)

# Escrita de dados
handler.write(df, table_name="clientes_backup")