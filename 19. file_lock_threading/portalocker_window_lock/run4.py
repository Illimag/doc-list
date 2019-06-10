import portalocker
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

    data[turn_into_string] = [{'test4': 'testtest'}, {'urltest4': 'testtest'}]

    print data

    with open("master.json", "w") as outfile:
        portalocker.lock(outfile, portalocker.LOCK_EX)
        json.dump(data, outfile)
        portalocker.unlock(outfile)


    time.sleep(random_sleep)