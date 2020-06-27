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

    ''' Current Weather Data '''
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

    def getCurrentRain1H(self):            
        try:
            return self.data['current']['rain']['1h']
        except:
            return None

    def getCurrentRain3H(self):            
        try:
            return self.data['current']['rain']['3h']
        except:
            return None

    def getCurrentSnow1H(self):            
        try:
            return self.data['current']['snow']['1h']
        except:
            return None

    def getCurrentSnow3H(self):            
        try:
            return self.data['current']['snow']['3h']
        except:
            return None

    ''' Minutely Forecast '''
    def getMinutelyForecast(self, index=0, format_time='default'):
        if format_time == 'default':
            dt = time.ctime(self.data['minutely'][index]['dt'])
        if format_time == 'minutely':
            dt = time.strftime('%H:%M', time.localtime(self.data['minutely'][index]['dt']))        
            
        precipitation = self.data['minutely'][index]['precipitation']

        return (dt, precipitation)

    def getMinutelyForecastCount(self):
        return len(self.data['minutely'])

    ''' Hourly Forecast '''
    def getHourlyForecast(self, index=0):
        dt = self.data['hourly'][index]['dt']
        dt = time.ctime(dt)

        temp = self.data['hourly'][index]['temp']
        feels_like = self.data['hourly'][index]['feels_like']
        pressure = self.data['hourly'][index]['pressure']
        humidity = self.data['hourly'][index]['humidity']
        dew_point = self.data['hourly'][index]['dew_point']
        clouds = self.data['hourly'][index]['clouds']
        wind_speed = self.data['hourly'][index]['wind_speed']
        wind_deg = self.data['hourly'][index]['wind_deg']
        weather_id = self.data['hourly'][index]['weather'][0]['id']
        weather_main = self.data['hourly'][index]['weather'][0]['main']
        weather_description = self.data['hourly'][index]['weather'][0]['description']
        weather_icon = self.data['hourly'][index]['weather'][0]['icon']
                    
        try:
            rain = self.data['hourly'][index]['rain']['1h']
        except:
            rain = None

        try:
            snow =  self.data['hourly'][index]['snow']['1h']
        except:
            snow = None

        return (dt, temp, feels_like, pressure, humidity, dew_point, clouds, wind_speed, wind_deg, rain, snow)
        
    def getHourlyForecastCount(self):
        return len(self.data['hourly'])

    ''' Daily Forecast '''
    def getDailyForecast(self, index=0):
        dt = time.ctime(self.data['daily'][index]['dt'])        
        sunrise = time.ctime(self.data['daily'][index]['sunrise'])                
        sunset = time.ctime(self.data['daily'][index]['sunset'])
        temp_min = self.data['daily'][index]['temp']['min']
        temp_max = self.data['daily'][index]['temp']['max']
        # skipped some data
        pressure = self.data['daily'][index]['pressure']
        humidity = self.data['daily'][index]['humidity']
        dew_point = self.data['daily'][index]['dew_point']
        wind_speed = self.data['daily'][index]['wind_speed']
        wind_deg = self.data['daily'][index]['wind_deg']
        weather_id = self.data['daily'][index]['weather'][0]['id']
        weather_main = self.data['daily'][index]['weather'][0]['main']
        weather_description = self.data['daily'][index]['weather'][0]['description']
        weather_icon = self.data['daily'][index]['weather'][0]['icon']
        clouds = self.data['daily'][index]['clouds']
        uvi = self.data['daily'][index]['uvi']
                    
        try:
            rain = self.data['daily'][index]['rain']['1h']
        except:
            rain = None

        try:
            snow =  self.data['daily'][index]['snow']['1h']
        except:
            snow = None

        return (dt, sunrise, sunset, temp_min, temp_max, pressure, humidity, dew_point, wind_speed, wind_deg, weather_description, clouds, uvi)
        
    def getDailyForecastCount(self):
        return len(self.data['daily'])

    def printCurrentWeatherReport(self):
        print('Weather coordinates: [{}, {}]'.format(self.getLatitude(),
                                         self.getLongitude()
                                         )
              )
        print('Timezone: {}'.format(self.getTimezone()))
        print('Timezone Offset: {}'.format(self.getTimeZoneOffset()))
        print('Local Time: {}'.format(self.getCurrentDate()))
        print('Sunrise: {}'.format(self.getCurrentSunrise()))
        print('Sunset: {}'.format(self.getCurrentSunset()))
        print('Description: {}'.format(self.getCurrentWeatherDescription()))
        print('Temperature: {} °F'.format(self.getCurrentTemperature()))
        print('Feels Like: {} °F'.format(self.getCurrentFeelsLike()))
        print('Pressure: {} hpa'.format(self.getCurrentPressure()))
        print('Humidity: {}%'.format(self.getCurrentHumidity()))
        print('Rain: {} mm/h'.format(self.getCurrentRain1H()))
        print('Snow: {} mm/h'.format(self.getCurrentSnow1H()))
        print('Dew Point: {} °F'.format(self.getCurrentDewPoint()))
        print('UV Index: {}'.format(self.getCurrentUVI()))
        print('Cloudiness: {}%'.format(self.getCurrentClouds()))
        print('Visibility: {:.2f} mi'.format(self.getCurrentVisibility()))
        print('Wind Speed: {} m/h, Direction: {}°'.format(self.getCurrentWindSpeed(),
                                                          self.getCurrentWindDegrees())
              )
        
        print()

        self.graphMinutelyForecast()

    def printMinutelyForecastReport(self):
        for idx in range(0, self.getMinutelyForecastCount()):
            print('Minutely[{}]: {}'.format(idx,self.getMinutelyForecast(idx)))
        print()

    def printHourlyForecastReport(self):
        for idx in range(0, self.getHourlyForecastCount()):
            print('Hourly[{}]: {}'.format(idx, self.getHourlyForecast(idx)))
        print()

    def printDailyForecastReport(self):
        for idx in range(0, self.getDailyForecastCount()):
            print('Daily[{}]: {}'.format(idx, self.getDailyForecast(idx)))
        print()

    def graphMinutelyForecast(self):
        precipitation_list = []
        precipitation_total = 0
        for idx in range(0, self.getMinutelyForecastCount()):
            minutely_data = self.getMinutelyForecast(idx, format_time='minutely')
            precipitation_time = minutely_data[0]
            precipitation_data = minutely_data[1]
            # print('{} {} mm/h'.format(precipitation_time, precipitation_data))
            precipitation_total = precipitation_total + precipitation_data
            precipitation_list.append((precipitation_time, precipitation_data))

        print("MINUTELY FORECAST ->")
        if precipitation_total == 0:
            print("No precipitation within an hour")
        else:
            print('{} {} mm/h'.format(precipitation_list[0], precipitation_list[1]))
            
        print()
        
    def saveCurrentWeatherData(self):
        directory = 'data'
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        filename = 'forecast_request' + '-' + time.strftime("%Y%m%d") + '-' + time.strftime("%H%M%S") + '.json'
        with open(os.path.join(directory, filename), 'w') as write_data:
            write_data.write(str(self.data))
            
    def __str__(self):
        return 'Current Weather Data = {}'.format(self.data)


class TimeMachineRequest(CurrentWeatherData):

    def __init__(self, year='1970', month='01', date='01', hour='00', minute='00', second='00'):
        
        CurrentWeatherData.__init__(self)
        self.year = year
        self.month = month
        self.date = date
        self.hour = hour
        self.minute = minute
        self.second = second

        self.data = self.getTimeMachineRequest(self.getDateTimeInSeconds())

    def getDateTimeInSeconds(self):
        s = self.month + '/' + self.date + '/' + self.year + ' ' + self.hour + ':' + self.minute + ':' + self.second
        return int(datetime.datetime.strptime(s, "%m/%d/%Y %H:%M:%S").strftime("%s"))

    def getTimeMachineRequest(self, dt):        
        http_request = 'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=' + self.lat + '&lon=' + self.lon + '&dt=' + str(dt) + '&APPID=' + self.key + '&units=imperial'
        # print('HTTP request: {}'.format(http_request))   
        res = requests.get(http_request)
        #print(res.json())
        return res.json()
