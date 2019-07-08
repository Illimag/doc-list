# Import requests
import requests
# Import pandas
import pandas as pd
# Import seaborn
import seaborn as sns
sns.set()
# Import matplotlib
import matplotlib.pyplot as plt

# Build base URL
HOST = "https://api.census.gov/data"
year = "2010"
dataset = "dec/sf1"
base_url = "/".join([HOST, year, dataset])
# https://api.census.gov/data/2010/dec/sf1

# Specify Census variables and other predicates

# "P013001" (median age)
# "P037001" (average family size)

get_vars = ["NAME", "P013001", "P037001"]
predicates = {}
predicates["get"] = ",".join(get_vars)
predicates["for"] = "state:*"

# Execute the request, examine text of response object
r = requests.get(base_url, params=predicates)
#print(r.text)
# Now we have the data object "r"
# Let's build the data frame

# Construct the data frame
col_names = ["name", "median_age", "avg_family_size", "state"]
states = pd.DataFrame(columns = col_names, data = r.json()[1:])

# Convert each column with numeric data to an appropriate type
states["median_age"] = states["median_age"].astype(float)
states["avg_family_size"] = states["avg_family_size"].astype(float)

# Scatterplot with regression line
sns.lmplot(x = "avg_family_size", y = "median_age", data = states)
plt.show()