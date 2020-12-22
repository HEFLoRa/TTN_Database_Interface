import shutil

# Gets inputs from local ttn_thing_registration component for testing purposes
original = '/home/konrad/Desktop/HEFLoRa/Components/TTN_thing_registration/output/device_registration_parameters_ttn.txt'
target = '/home/konrad/Desktop/HEFLoRa/Components/TTN_database_interface/configs/scenarios/input_ttn.json'

shutil.copyfile(original, target)