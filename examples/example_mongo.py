from my_data_lib.factory import get_data_handler

# Crie o handler usando a factory
handler = get_data_handler(
    "mongodb",
    uri="mongodb://localhost:27017",
    database="meubanco",
    collection="clientes"
)

# Leitura de dados
df = handler.read(filter_query={"status": "ativo"})
print(df)

# Escrita de dados
handler.write(df)