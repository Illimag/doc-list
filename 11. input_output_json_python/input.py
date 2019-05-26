import json

with open('data.json') as json_file:  
    data = json.load(json_file)
    print data

    lead = (data["0"])
    print lead

    title = lead[0]
    print title

    test_title = title["title"]
    print test_title
