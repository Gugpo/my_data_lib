# from unittest.mock import MagicMock, patch
# import pytest
# import pandas as pd
# import psycopg2.extras
# from my_data_lib.postgres_handler import PostgresHandler

# @pytest.fixture
# def mock_psycopg2_connect():
#     with patch("my_data_lib.postgres_handler.psycopg2.connect") as mock_connect:
#         mock_conn = mock_connect.return_value
#         mock_cursor = mock_conn.cursor.return_value

#         # Mock do fetchall para retornar dados de exemplo
#         mock_cursor.fetchall.return_value = [(1, "teste1"), (2, "teste2")]
#         mock_cursor.description = (("id",), ("nome",))

#         yield mock_connect

# def test_postgres_read_write(mock_psycopg2_connect):
#     handler = PostgresHandler(
#         connection_string="postgresql://user:password@localhost:5432/testdb",
#         table_name="minha_tabela"
#     )
    
#     df = handler.read()
#     assert not df.empty
#     # assert "nome" in df.columns

#     # Testa write, verifica se executou commit
#     handler.write(df)
#     mock_psycopg2_connect.return_value.cursor.return_value.execute.assert_called()
#     mock_psycopg2_connect.return_value.commit.assert_called_once()
