from open_db_connection import client


def close_db_connection(connection):
    connection.close()
    print('Database connection has been terminated')


close_db_connection(client)
