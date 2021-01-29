import shutil

# Gets inputs from local ttn_thing_registration component for testing purposes
original = '/home/konradb/Desktop/HEF/Workshops/5_Workshop/Demo/TTN_thing_registration-main/output/device_registration_parameters_ttn.txt'
target = '/home/konradb/Desktop/HEF/Workshops/5_Workshop/Demo/TTN_Database_Interface/configs/scenarios/input_ttn.json'
shutil.copyfile(original, target)

# Gets input from local frost_cli component for testing purposes
original = '/home/konradb/Desktop/HEF/Workshops/5_Workshop/Demo/FROST_CLI-main/output/device_registration_parameters_frost.txt'
target = '/home/konradb/Desktop/HEF/Workshops/5_Workshop/Demo/TTN_Database_Interface/configs/scenarios/input_frost.json'
shutil.copyfile(original, target)


