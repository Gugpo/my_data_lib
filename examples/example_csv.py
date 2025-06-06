from my_data_lib.factory import get_data_handler

# Crie o handler usando a factory
handler = get_data_handler("csv", path="data/exemplo.csv")

# Leitura dos dados do CSV
df = handler.read()
print(df.head())

# Escrita de dados
handler.write(df)