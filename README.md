# weather_scraper

Geo_Requests:
It all starts with Geo_Requests. There are several ways that OpenWeather will allow you to specify the location for which you want the weather, and using coordinates (longitude and latitude) is just one of those ways. In order to get more practice making requests from the OpenWeather API, I chose to make requesting the coordinates for a city a part of my repo, though it is completely redundant. The Geo_Requests folder essentially just asks OpenWeather what the coordinates are for Bakersfield, New York City, Amissville, and Medellin, then stores that information in a variable so that it can be easily extracted in the request for the weather

func_get_weather.py
This file only defines the get_weather() function. This function takes the coordiantes, makes 4 weather requests to OpenWeather.com, parses out the information that I want, and writes it to New_Weather.csv along with the timestamp for the date and time that the request was made. New_Weather.csv is overwritten each time the get_weather() function is ran, so it only contains the information from the most recent request.

gsheet.py
This python file has a few different jobs. It makes a connection to a Google Sheet using Google's API, uses the get_weather() function to get the weather, transforms the dataframe into an array of arrays and appends it to the end of the Google Sheet so that the Google Sheet keeps a log of each request made. 

get_weather.sh
This is a script that simply runs gsheet.py. On my computer a cronjob is programmed to run this file every 30 minutes (when my computer is on and running) as to keep an accurate log of the current(ish) weather.

SECRETS: 
What isn't included in this repo is also important if you wanted to copy what I've done. 

Tableau: I've created a tableau dash board that displays on a map the weather that I've requested. The sad part is that with the free version of Tableau, I can't automatically update the data. In order to keep it up to date with the free version, I would have to open the Tableau workbook as often as the requests are made, and I'm just not going to do that. https://public.tableau.com/views/WeatherDash/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link

OpenWeather API Key: This is free from OpenWeather. I didn't include it for obvious reasons. 
Google Sheets API Credentials and Token. For obvious reasons, my credentials and token are not here, but again, if you wanted to copy me, you'll need your own Google account with the Sheets API activated as well. I used this video from Daniel Otto to help me learn how to work with the google sheets API: 
https://www.youtube.com/watch?v=X-L1NKoEi10&pp=ygUYZ29vZ2xlIHNoZWV0cyBhcGkgZGFuaWVs. 
