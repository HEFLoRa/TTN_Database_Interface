import json
import os
from configs.database_connection import cur, conn
from unique_thing_id.id_generator import id

# Calls get_input to get data from ttn_thing_registration
os.system('python3 configs/scenarios/get_input.py')

# Gets input and stores it in variable
input = open("configs/scenarios/input_ttn.json")
input_data = json.load(input)

cur.execute("INSERT INTO thing VALUES(%s, 'test', 'test', 10, null, 10, true);" % (str(id)))
conn.commit()

cur.execute("SELECT * FROM thing")
result = cur.fetchall()

cur.close()
conn.close()

print(result)


