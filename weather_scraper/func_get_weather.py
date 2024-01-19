import requests 
import pandas as pd
from datetime import datetime
import pytz
# This line imports my API Key from a hidden file on my computer. Replace the variable Key with your own 
    # OpenWeather API key
from ignore.OpenWeatherAPI import Key

def get_weather():
    # Import dataset with latitudes and longitudes
    file_path="~/repos/weather_scraper/Geo_Requests/geolocations.csv"
    df = pd.read_csv(file_path, index_col=0)

    # Build bones of OpenWeather request:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat="
    API_KEY=Key

    # Create new columns for the data that I want
    df['weather_description'] = ''
    df['temperature'] = ''
    df['temp_feels_like'] = 0
    df['humidity'] = 0
    df['wind_speed'] = 0
    df['wind_direction'] = 0
    df['date'] = ''


    #### Create new data frame called todays_weather to hold new weather data. This will be merged 
    todays_weather = pd.DataFrame() 
    columns = ['City',
            'weather_description',
            'temp(F)',
            'feels_like(F)',
            'humidity', 
            'speed', 
            'deg',
            'forecast_min',
            'forecast_max']

    for col in columns: 
        todays_weather[col]=''

    # select the values that I want: 
    desired_values = [['weather','description'], ['main','temp'], ['main','feels_like'], ['main','humidity'], 
            ['wind','speed'], ['wind','deg'], ['main', 'temp_min'], ['main', 'temp_max']]

    # use a for-loop to send requests and extract information into column
        
    # Make request for each location. Each request is a dictionary called 'response'
    for j in range(len(df)):
        lat = df.loc[j,'latitude'].astype(str)
        lon = df.loc[j,'longitude'].astype(str)

        url = BASE_URL + lat + "&lon=" + lon  + "&appid="  + API_KEY + "&units=imperial"

        response = requests.get(url).json()
        
        # Extract the information that I need from response and place into list
        city = df.loc[j,'City']
        newcity_info = [city]
        for i in range(len(desired_values)):
            a = desired_values[i][0]
            b = desired_values[i][1]
            if a == 'weather':
                value = response[a][0][b]
                newcity_info.append(value)
            else: 
                value = response[a][b]
                newcity_info.append(value)

        # input list into new dataframe, todaysweather
        todays_weather.loc[j] = newcity_info
    
    #input timezones:
    timezones=['US/Pacific', 'US/Eastern', 'US/Eastern', 'Etc/GMT+5']
    todays_weather['Timezone']=timezones

    # input time
    todays_weather['Time']=''

    for i in range(len(todays_weather)):
        current_time = datetime.now(pytz.timezone(todays_weather.loc[i,'Timezone']))
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M')
        todays_weather.loc[i,'Time']=formatted_time

    # Merge df an todays weather to include State, Country, latitude and longitude
    df=df[['latitude', 'longitude', 'Country', 'State','City']]
    
    todays_weather=df.merge(todays_weather, on="City")
    todays_weather.to_csv("New_Weather.csv", index=False)

    return True

get_weather()
