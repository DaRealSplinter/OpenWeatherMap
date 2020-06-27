#!/usr/bin/env python3
import OpenWeatherMap
import argparse

def main():

    cmd_parser = argparse.ArgumentParser(description='Get the weather forecast')
    cmd_parser.add_argument('-s', action='store_true', help='save the forecast request to a json file')
    cmd_parser.add_argument('-M', action='store_true', help='print the minutely forecast request')
    cmd_parser.add_argument('-H', action='store_true', help='print the hourly forecast request')
    cmd_parser.add_argument('-D', action='store_true', help='print the daily forecast request')
    
    args = cmd_parser.parse_args()

    # always print the current weather report
    report = OpenWeatherMap.CurrentWeatherData()
    report.printCurrentWeatherReport()

    if args.s:
        report.saveCurrentWeatherData()
        print()

    if args.M:
        report.formattedMinutelyForecastReport()

    if args.H:
        report.printHourlyForecastReport()

    if args.D:
        report.printDailyForecastReport()
    
    print('Powered by OpenWeatherMap: https://openweathermap.org/')
    
    
if __name__ == '__main__':
    main()
