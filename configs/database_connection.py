import psycopg2

# Connects to (local) database
conn = psycopg2.connect(
    host="localhost",
    database="things_v2",
    user="postgres",
    password="main123456"
)

# Opens cursor to perform database operations
cur = conn.cursor()
