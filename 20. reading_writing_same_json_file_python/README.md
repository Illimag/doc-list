# Reading Writing same JSON file with Python

This is how to read a json file with python.

First need to have json imported.

	import json

Now we can use this functionality in a python script.
	
	with open("json.json", 'r') as json_file:
	    json_object = json.load(json_file)

We open the json file to load the json object to a var in the python script.

To write a json file with python change the 'r' to a 'w'

	with open("json.json", 'w') as json_file:
	    json.dump(json_object,json_file)

We open the file to overwrite the json object to the json_file.

Important to note that the files will close by themselves after they leave scope.

Now to write and read the same json file without closing the file we need to use 'r+'

As well as using

	.seek()

	.truncate()

So in this example:

	with open("json.json", 'r+') as json_file:
	    json_object = json.load(json_file)
	    #Make edits to json_object
	    json_file.seek(0)
	    json.dump(json_object, json_file)
	    json_file.truncate()

We open the json file and load it to a json object.

After the changes are completed on the json object.

We seek the start of the json file and then overwrite the json file with the eddited json object.

We then truncate in case the new data is smaller than the old data.

Finally we exit and the file will close.

This is particularly useful combined with a lock and unlocking system.

The following is an example of where the file is locked before loading.

Then after all processes are complete the file will unlock, allowing other programs to utilize the file.

This demo is with portalocker.

More information on portalocker in:

	[19. file_lock_threading]

Portalocker is a cross-platform(windows and linux) locking and unlocking python dependency.

	with open("json.json", 'r+') as json_file:
		portalocker.lock(json_file, portalocker.LOCK_EX)
	    json_object = json.load(json_file)
	    #Make edits to json_object
	    json_file.seek(0)
	    json.dump(json_object, json_file)
	    json_file.truncate()
		portalocker.unlock(json_file)