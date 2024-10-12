import pyodbc


class AccessWriter:
    def __init__(self):
        pass

    def write_all(self, db_filepath: str, table_name: str, table_shema: list[str], records: list[list[str]]):
        connection = self._connect(db_filepath)
        if connection is not None:
            shema = ""
            for shema_field in table_shema:
                shema += shema_field + ", "
            shema = shema[:-2]
            query = f"""
                CREATE TABLE {table_name} ({shema})
                """

            # execute

            query = f"""
                INSERT INTO {table_name}
            """
            for record in records:
                data = ""
                for data_field in record:
                    data += data_field + ", "
                data = data[:-2]
                query += f"\n({data})\n"

            # execute

            connection.close()

    def _connect(self, db_filepath: str) -> pyodbc.Connection | None:
        conn_str = (
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
            f"DBQ={db_filepath};"
        )
        try:
            connection = pyodbc.connect(conn_str)
            return connection
        except pyodbc.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")
            return None
