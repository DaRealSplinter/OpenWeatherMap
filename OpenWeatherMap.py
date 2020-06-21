import KeyParser
import requests
import datetime
import time
import os

class CurrentWeatherData:

    def __init__(self):
        key_file = KeyParser.OpenWeatherMap()
        self.key = key_file.getKey()
        self.name = key_file.getName()
        self.lat = key_file.getLatitude()
        self.lon = key_file.getLongitude()

        self.data = self.getWeatherData()

    def getWeatherData(self):
        http_request = 'http://api.openweathermap.org/data/2.5/onecall?lat=' + self.lat + '&lon=' + self.lon + '&APPID=' + self.key + '&units=imperial'
                
        res = requests.get(http_request)
        return res.json()

    def getLatitude(self):
        return self.data['lat']

    def getLongitude(self):
        return self.data['lon']

    def getCoordinates(self):
        lat = self.getLatitude()
        lon = self.getLongitude()
        return [lat, lon]

    def getTimezone(self):
        return self.data['timezone']

    def getTimeZoneOffset(self):
        return self.data['timezone_offset']

    def getCurrentDate(self):
        return datetime.datetime.fromtimestamp(self.data['current']['dt'])

    def getCurrentSunrise(self):
        return time.ctime(self.data['current']['sunrise'])

    def getCurrentSunset(self):
        return time.ctime(self.data['current']['sunset'])

    def getCurrentTemperature(self):
        return self.data['current']['temp']

    def getCurrentFeelsLike(self):
        return self.data['current']['feels_like']

    def getCurrentPressure(self):
        return self.data['current']['pressure']

    def getCurrentHumidity(self):
        return self.data['current']['humidity']

    def getCurrentDewPoint(self):
        return self.data['current']['dew_point']

    def getCurrentUVI(self):
        return self.data['current']['uvi']

    def getCurrentClouds(self):
        return self.data['current']['clouds']

    def getCurrentVisibility(self):
        return self.data['current']['visibility'] / 1609.344  # MI

    def getCurrentWindSpeed(self):
        return self.data['current']['wind_speed']

    def getCurrentWindDegrees(self):
        return self.data['current']['wind_deg']

    def getCurrentWeatherId(self):
        return self.data['current']['weather'][0]['id']

    def getCurrentWeatherMain(self):
        return self.data['current']['weather'][0]['main']

    def getCurrentWeatherDescription(self):
        return self.data['current']['weather'][0]['description']

    def getCurrentWeatherIcon(self):
        return self.data['current']['weather'][0]['icon']

    def getBase(self):
        return self.data['base']

    def getMainTemperature(self):
        return self.data['main']['temp']

    def getMainPressure(self):
        return self.data['main']['pressure']  # hPa

    def getMainHumidity(self):
        return self.data['main']['humidity']

    def getMainTemperatureMinimal(self):
        return self.data['main']['temp_min']

    def getMainTemperatureMaximal(self):
        return self.data['main']['temp_max']

    def getVisibility(self):
        return self.data['visibility'] / 1609.344  # MI

    def getWindSpeed(self):
        return self.data['wind']['speed']

    def getWindGust(self):
        try:
            return self.data['wind']['gust']
        except:
            return None

    def getWindBearing(self):            
        try:
            return self.data['wind']['deg']
        except:
            return None

    def getCloudsAll(self):
        return self.data['clouds']['all']

    def getDate(self):
        return datetime.datetime.fromtimestamp(self.data['dt'])

    def getSystemType(self):
        return self.data['sys']['type']

    def getSystemId(self):
        return self.data['sys']['id']

    def getSystemCountry(self):
        return self.data['sys']['country']

    def getSystemSunrise(self):
        return time.ctime(self.data['sys']['sunrise'])

    def getSystemSunset(self):
        return time.ctime(self.data['sys']['sunset'])

    def getTimezone(self):
        return self.data['timezone']

    def getId(self):
        return self.data['id']

    def getName(self):
        return self.data['name']

    def getCod(self):
        return self.data['cod']

    def getRain1H(self):            
        try:
            return self.data['rain']['1h']
        except:
            return None

    def getRain3H(self):            
        try:
            return self.data['rain']['3h']
        except:
            return None

    def getSnow1H(self):            
        try:
            return self.data['snow']['1h']
        except:
            return None

    def getSnow3H(self):            
        try:
            return self.data['snow']['3h']
        except:
            return None

    def printCurrentWeatherData(self):
        print('Currently weather data:\n' \
              'Coordinates: {}\n' \
              'Weather Id: {}\n' \
              'Weather Main: {}\n' \
              'Weather Description: {}\n' \
              'Weather Icon: {}\n' \
              'Base: {}\n' \
              'Main Temperature: {}\n' \
              'Main Pressure: {}\n' \
              'Main Humidity: {}\n' \
              'Main Min. Temperature: {}\n' \
              'Main Max. Temperature: {}\n' \
              'Visibility: {}\n' \
              'Wind Speed: {}\n' \
              'Wind Gust: {}\n' \
              'Wind Bearing: {}\n' \
              'Cloud All: {}\n' \
              'Date: {}\n' \
              'System Type: {}\n' \
              'System Id: {}\n' \
              'System Country: {}\n' \
              'System Sunrise: {}\n' \
              'System Sunset: {}\n' \
              'Timezone: {}\n' \
              'Id: {}\n' \
              'Name: {}\n' \
              'Cod: {}\n' \
              'Rain 1H: {}\n' \
              'Rain 3H: {}\n' \
              'Snow 1H: {}\n' \
              'Snow 3H: {}\n'
              .format(self.getCoordinates(),
                      self.getWeatherId(),
                      self.getWeatherMain(),
                      self.getWeatherDescription(),
                      self.getWeatherIcon(),
                      self.getBase(),
                      self.getMainTemperature(),
                      self.getMainPressure(),
                      self.getMainHumidity(),
                      self.getMainTemperatureMinimal(),
                      self.getMainTemperatureMaximal(),
                      self.getVisibility(),
                      self.getWindSpeed(),
                      self.getWindGust(),
                      self.getWindBearing(),
                      self.getCloudsAll(),
                      self.getDate(),
                      self.getSystemType(),
                      self.getSystemId(),
                      self.getSystemCountry(),
                      self.getSystemSunrise(),
                      self.getSystemSunset(),
                      self.getTimezone(),
                      self.getId(),
                      self.getName(),
                      self.getCod(),
                      self.getRain1H(),
                      self.getRain3H(),
                      self.getSnow1H(),
                      self.getSnow3H()
                  )
              )

    def printCurrentWeatherReport(self):
        print('Weather coordinates {}, {}'.format(self.getLatitude(),
                                         self.getLongitude()
                                         )
              )
        print('Timezone: {}'.format(self.getTimezone()))
        print('Timezone Offset: {}'.format(self.getTimeZoneOffset()))
        print('Local Time: {}'.format(self.getCurrentDate()))
        print('Sunrise: {}'.format(self.getCurrentSunrise()))
        print('Sunset: {}'.format(self.getCurrentSunset()))
        print('Temperature: {} °F'.format(self.getCurrentTemperature()))
        print('Feels Like: {} °F'.format(self.getCurrentFeelsLike()))
        print('Pressure: {} hpa'.format(self.getCurrentPressure()))
        print('Humidity: {}%'.format(self.getCurrentHumidity()))
        print('Dew Point: {} °F'.format(self.getCurrentDewPoint()))
        print('UV Index: {}'.format(self.getCurrentUVI()))
        print('Cloudiness: {}%'.format(self.getCurrentClouds()))
        print('Visibility: {:.2f} mi'.format(self.getCurrentVisibility()))
        print('Wind Speed: {} m/h, Direction: {}°'.format(self.getCurrentWindSpeed(),
                                                          self.getCurrentWindDegrees())
              )
##        print('{} °F\n{}\n{}'.format(self.getMainTemperature(),
##                                     self.getWeatherDescription(),
##                                     self.getDate()
##                                     )
##              )
##        print('Wind: {} m/h, Direction: {}°, Gust: {}'.format(
##                self.getWindSpeed(),
##                self.getWindBearing(),
##                self.getWindGust()
##                )
##              )
##        print('Cloudiness: {}%'.format(self.getCloudsAll()))
##        print('Pressure: {} hpa'.format(self.getMainPressure()))
##        print('Humidity: {}%'.format(self.getMainHumidity()))
##        print('Rain: {} mm'.format(self.getRain1H()))
##        print('Snow: {} mm'.format(self.getSnow1H()))
##        print('Visibility: {:.2f} mi'.format(self.getVisibility()))
##        print('Sunrise: {}'.format(self.getSystemSunrise()))
##        print('Sunset: {}'.format(self.getSystemSunset()))
##        print('Geo coordinates: {}'.format(self.getCoordinates()))
        print()
##        print(self.__str__())
##        print()
        

    def saveCurrentWeatherData(self):
        directory = 'data'
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        filename = 'forecast_request' + '-' + time.strftime("%Y%m%d") + '-' + time.strftime("%H%M%S") + '.json'
        with open(os.path.join(directory, filename), 'w') as write_data:
            write_data.write(str(self.data))
            
    def __str__(self):
        return 'Current Weather Data = {}'.format(self.data)
