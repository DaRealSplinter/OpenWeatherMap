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
     alerts=COUNTY_CODE_LINK
     ```
     The id, lat, and lon are NOT used in the application but are still called for future uses, if desired.

 4. Run the application - *Main.py* runs in a terminal with options.
 
 ## Release Notes ##
 3.0.0 - OpenWeather does NOT have the alerts available in the API like DarkSky. Alerts are now available using https://alerts.weather.gov/. Click on **By State/County...** under the **Warnings** sections. Then click on **County List** by the desired state in the **State (Zone List | County List)** list. Lastly, click on the **County Code** by the desired **County Name** in the list. This will be the link for the alerts app.
 
 2.1.0 - Better presentation of the current weather and the minutely, hourly and daily forecast.
 
 2.0.0 - OpenWeather now has an API similar to DarkSky to get free access to main weather data such as current weather, forecast (minutely, hourly, daily) and historical weather up to five previous days (time-machine) with only one call to the API.
 
 1.0.0 - Initial release. This project was copied from my original repository. 

#### References ####
* [List of Trees](https://www.treenames.net/common_tree_names.html)
