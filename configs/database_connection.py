import psycopg2

# Connects to (local) database
try:
    conn = psycopg2.connect(
    host="localhost",
    database="things_v2",
    user="postgres",
    password="main123456"
    )
except:
    print('Unable to connect')

# Opens cursor to perform database operations
cur = conn.cursor()