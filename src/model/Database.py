import sqlalchemy as sa
class Database:
    def connecta_database(self):    
        user = input('Usuário: ')
        password = input('Senha: ')
        password = 'python'
        server = 'DESKTOP-3ULV54Q\SQLEXPRESS'
        database = 'Vagas'
        driver = 'ODBC Driver 18 for SQL Server'
        conn_string = f'mssql+pyodbc://{user}:{password}@{server}/{database}?TrustServerCertificate=yes&trusted_connection=yes&driver={driver}&protocol=namedpipes'
        engine = sa.create_engine(conn_string)
        return engine
