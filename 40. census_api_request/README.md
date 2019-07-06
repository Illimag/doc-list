# Census API Request

## This is how to do a simple API request to the US government census website.

First import requests

	import requests
Build the base URL.

	HOST = "https://api.census.gov/data"
	year = "2010"
	dataset = "dec/sf1"
	base_url = "/".join([HOST, year, dataset])

This will build the URL as following.

	https://api.census.gov/data/2010/dec/sf1

Specify the census variables.

# "P013001" (median age)

# "P037001" (average family size)

	get_vars = ["NAME", "P013001", "P037001"]
	predicates = {}
	predicates["get"] = ",".join(get_vars)
	predicates["for"] = "state:*"

Now do the API request.

	r = requests.get(base_url, params=predicates)

Now print out the output as text.

	print(r.text)

This is what will print.

	[["NAME","P013001","P037001","state"],
	["Alabama","37.9","3.02","01"],
	["Alaska","33.8","3.21","02"],
	["Arizona","35.9","3.19","04"],
	["Arkansas","37.4","3.00","05"],
	["California","35.2","3.45","06"],
	["Louisiana","35.8","3.10","22"],
	["Kentucky","38.1","2.98","21"],
	["Colorado","36.1","3.08","08"],
	["Connecticut","40.0","3.08","09"],
	["Delaware","38.8","3.06","10"],
	["District of Columbia","33.8","3.01","11"],
	["Florida","40.7","3.01","12"],
	["Georgia","35.3","3.17","13"],
	["Hawaii","38.6","3.42","15"],
	["Idaho","34.6","3.16","16"],
	["Illinois","36.6","3.20","17"],
	["Indiana","37.0","3.05","18"],
	["Iowa","38.1","2.97","19"],
	["Kansas","36.0","3.06","20"],
	["Maine","42.7","2.83","23"],
	["Maryland","38.0","3.15","24"],
	["Massachusetts","39.1","3.08","25"],
	["Michigan","38.9","3.05","26"],
	["Minnesota","37.4","3.05","27"],
	["Mississippi","36.0","3.11","28"],
	["Missouri","37.9","3.00","29"],
	["Montana","39.8","2.91","30"],
	["Nebraska","36.2","3.04","31"],
	["Nevada","36.3","3.20","32"],
	["New Hampshire","41.1","2.96","33"],
	["New Jersey","39.0","3.22","34"],
	["New Mexico","36.7","3.13","35"],
	["New York","38.0","3.20","36"],
	["North Carolina","37.4","3.01","37"],
	["North Dakota","37.0","2.91","38"],
	["Ohio","38.8","3.01","39"],
	["Oklahoma","36.2","3.04","40"],
	["Oregon","38.4","3.00","41"],
	["Pennsylvania","40.1","3.02","42"],
	["Rhode Island","39.4","3.04","44"],
	["South Carolina","37.9","3.01","45"],
	["South Dakota","36.9","3.00","46"],
	["Tennessee","38.0","3.01","47"],
	["Texas","33.6","3.31","48"],
	["Utah","29.2","3.56","49"],
	["Vermont","41.5","2.85","50"],
	["Virginia","37.5","3.06","51"],
	["Washington","37.3","3.06","53"],
	["West Virginia","41.3","2.88","54"],
	["Wisconsin","38.5","2.99","55"],
	["Wyoming","36.8","2.96","56"],
	["Puerto Rico","36.9","3.17","72"]]