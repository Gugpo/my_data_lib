from typing import Literal, Union
from .csv_handler import CSVHandler
from .postgres_handler import PostgresHandler
from .mongodb_handler import MongoDBHandler

def get_data_handler(
    source_type: Literal["csv", "postgres", "mongodb"],
    **kwargs
) -> Union[CSVHandler, PostgresHandler, MongoDBHandler]:
    if source_type == "csv":
        return CSVHandler(**kwargs)
    elif source_type == "postgres":
        return PostgresHandler(**kwargs)
    elif source_type == "mongodb":
        return MongoDBHandler(**kwargs)
    else:
        raise ValueError(f"Fonte de dados '{source_type}' não suportada.")
