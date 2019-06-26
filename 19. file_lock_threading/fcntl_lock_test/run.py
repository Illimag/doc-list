import fcntl
import json
import time
import random

loop = True



while loop:

    random_sleep = (random.randint(1,10)*.1)
    time.sleep(random_sleep)

    with open("master.json", "r") as json_file:
        data = json.load(json_file)
        total_number_of_items_in_data = len(data)

    add_item = total_number_of_items_in_data
    turn_into_string = str(add_item)

    data[turn_into_string] = [{'test': 'testtest'}, {'urltest': 'testtest'}]

    print data

    with open("master.json", "w") as outfile:
        fcntl.flock(outfile, fcntl.LOCK_EX)
        json.dump(data, outfile)
        fcntl.flock(outfile, fcntl.LOCK_UN)


    time.sleep(random_sleep)