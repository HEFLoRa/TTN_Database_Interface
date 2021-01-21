import json
import os
from configs.database_connection import cur, conn


# Calls get_input to get data from ttn_thing_registration
os.system('python3 configs/scenarios/get_input.py')

# Gets input and stores it in variable
input = open("configs/scenarios/input_ttn.json")
input_data = json.load(input)

# Writes input in thing table
cur.execute("INSERT INTO thing VALUES(default, 'fake_user', 'fake_client', 01, null, null, true);")

# Pulls unique_thing_id from thing table
cur.execute("SELECT unique_thing_id FROM thing ORDER BY unique_thing_id DESC LIMIT 1")
id = cur.fetchall()

# TODO check for ttn -> source_ttn / source_third_party

# Writes input in source_ttn table
cur.execute("INSERT INTO source_ttn VALUES(%s, '%s', '%s', '%s', 'localhost:8080', null, '%s', '%s', 'localhost');" % (str(id[0][0]), input_data["Application ID"], input_data["Device ID"], input_data["Access Key"], input_data["DevEUI"], input_data["AppEUI"]))

conn.commit()
cur.close()
conn.close()
