# Pulls latest Id and updates it
file = open('unique_thing_id/CurrentId.txt', 'r+')
id = int(file.read())
file.seek(0)
file.truncate(0)
file.write(str(id+1))
file.close()
