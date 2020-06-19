# OpenWeatherMap
 A command-line based application that retrieves the weather forecast using the OpenWeatherMap API.

 ## Instructions ##
 1. Go to [https://openweathermap.org/api](https://openweathermap.org/api).
 2. Subscribe to the **Current weather data** collection.
 3. Create a **key.id** in the location as the EXE file with the following:

     ```
     [openweathermap]
     key=1234567890abcdef1234567890abcdef
     name=NAME_OF_CITY
     id=CITY_ID
     lat=CITY_LATITUDE
     lon=CITY_LONGITUDE
     ```
     The id, lat, and lon are NOT used in the application but are still called for future uses, if desired.

 4. Run the application - *Main.py* runs in a terminal with options and *MainDB.py* saves the data to a database as well as the JSON files.
 
 ## Release Notes ##
 2.0.0 - OpenWeather now has an API similar to DarkSky to get free access to main weather data such as current weather, forecast (minutely, hourly, daily) and historical weather up to five previous days (time-machine) with only one call to the API.
 1.0.0 - Initial release. This project was copied from my original repository. 

#### References ####
* [List of Trees](https://www.treenames.net/common_tree_names.html)
