from OpenWeatherMap import TimeMachineRequest
import argparse

def main():

    cmd_parser = argparse.ArgumentParser(description='Get the time machine request')
    cmd_parser.add_argument('-s', action='store_true', help='save the forecast request to a json file')
    cmd_parser.add_argument('-H', action='store_true', help='print the hourly forecast request')

    args = cmd_parser.parse_args()

    year = input('Year [YYYY]: ')
    month = input('Month [MM]: ')
    date = input('Date [DD]: ')
    hour = input('Hour [HH]: ')
    minute = input('Minute [MM]: ')
    second = input('Second [SS]: ')

    tm = TimeMachineRequest(year, month, date, hour, minute, second)
##    print(tm)
    tm.printCurrentWeatherReport()

    if args.s:
        tm.saveCurrentWeatherData()
        print()

    if args.H:        
        tm.printHourlyForecastReport()
        print()
        
    print('Powered by OpenWeatherMap: https://openweathermap.org/')


if __name__ == '__main__':
    main()
