# Import requests
import requests
# Import pandas
import pandas as pd
# Import matplotlib
import matplotlib.pyplot as plt
# Import seaborn
import seaborn as sns
sns.set()

# Build base URL
HOST = "https://api.census.gov/data"
year = "2010"
dataset = "dec/sf1"
base_url = "/".join([HOST, year, dataset])

# Specify variables and execute API request
get_vars = ["NAME", "PCT021005", "PCT021015"]
predicates = {}
predicates["get"] = ",".join(get_vars)
predicates["for"] = "state:*"
r = requests.get(base_url, params=predicates)

# Construct data frame
col_names = ["name", "in_adult", "in_juvenile", "state"]
states = pd.DataFrame(columns=col_names, data=r.json()[1:])
states[["in_adult", "in_juvenile"]] = states[["in_adult", "in_juvenile"]].astype(int)

# Calculate percentage of incarcerated male minors in adult facilities
states["pct_in_adult"] = ((100*states["in_adult"])/(states["in_adult"]+states["in_juvenile"]))
states.sort_values(by = "pct_in_adult", ascending = False, inplace = True)
sns.stripplot(x = "pct_in_adult", y = "name", data = states)
plt.show()
