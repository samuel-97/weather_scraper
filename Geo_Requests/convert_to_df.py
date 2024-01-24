from geocoder_requests import request_bin
import pandas as pd
import re

#Convert dictionary to Pandas DataFrame
keys = list(request_bin.keys())
inner_keys = ['lat', 'lon', 'country', 'state']
simple_dict = {}

for place in keys:
  simple_dict[place] = []
  for var in inner_keys:
    simple_dict[place].append(request_bin[place][0][var]) 
     
df = pd.DataFrame.from_dict(simple_dict,orient='index', columns = ['latitude', 'longitude', 'Country', 'State'])
df.reset_index(inplace = True, names = 'q')

#Clean City name

df['City'] = ''

for i in df.index:
  city = df['q'][i]
  result = re.search(r'(.*?),', city)
  newcity = result.group(1)
  df.at[i,'City'] = newcity


df.to_csv("Geo_Requests/geolocations.csv")

print(df)


