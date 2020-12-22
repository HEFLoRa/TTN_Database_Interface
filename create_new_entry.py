from configs.database_connection import cur

cur.execute('SELECT version()')