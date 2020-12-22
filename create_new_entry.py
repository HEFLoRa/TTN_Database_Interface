import json
import os
from configs.database_connection import cur, conn
from unique_thing_id.id_generator import id

# Calls get_input to get data from ttn_thing_registration
os.system('python3 configs/scenarios/get_input.py')

# Gets input and stores it in variable
input = open("configs/scenarios/input_ttn.json")
input_data = json.load(input)

# Writes input in thing table
cur.execute("INSERT INTO thing VALUES(%s, 'fake_user_%s', 'fake_client', 00, null, null, true);" % (str(id), str(id)))

# TODO check for ttn -> source_ttn / source_third_party

# Writes input in source_ttn table
cur.execute("INSERT INTO source_ttn VALUES(%s, '%s', '%s', '%s', 'fake_address', null);" % (str(id), input_data["Application ID"], input_data["Access Key"], input_data["Device ID"]))

conn.commit()

cur.execute("SELECT * FROM source_ttn")
result = cur.fetchall()

cur.close()
conn.close()

print(result)


