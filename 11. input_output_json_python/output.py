import json

data = { 
}

data[0] = []
data[1] = []
data[2] = []
data[3] = []

test_title = "this is a test title"
test_url = "test.com"
data[0].append({'title':test_title})
data[0].append({'url':test_url})

test_title1 = "this is a test title1"
test_url1 = "test.com1"
data[1].append({'title1':test_title1})
data[1].append({'url1':test_url1})

test_title2 = "this is a test title2"
test_url2 = "test.com2"
data[2].append({'title2':test_title2})
data[2].append({'url2':test_url2})

test_title3 = "this is a test title3"
test_url3 = "test.com3"
data[3].append({'title3':test_title3})
data[3].append({'url3':test_url3})
print data

with open('data.json', 'w') as outfile:  
    json.dump(data, outfile)
