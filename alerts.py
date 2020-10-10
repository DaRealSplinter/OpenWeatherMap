import requests
import KeyParser
from bs4 import BeautifulSoup

def weather_alerts():
    key_file = KeyParser.OpenWeatherMap()
    URL = key_file.getAlertsLink()
    page = requests.get(URL)
    data = page.content

    # get either the <id> or <link> element
    soup = BeautifulSoup(data, 'html.parser')
    results = soup.findAll('id')

    alerts = []
    for idx in results:
        try:
            link = idx.text
            page = requests.get(link)
            data = page.content
            soup = BeautifulSoup(data, 'html.parser')
            event = soup.find('event').text
            effective = soup.find('effective').text
            expires = soup.find('expires').text
            description = soup.find('description').text
            alert = (event, effective, expires, description, link)
            alerts.append(alert)
        except:
            pass

    return alerts

def main():
    alerts = weather_alerts()
    print('Alerts...')
    if len(alerts) != 0:
        for idx in range(0, len(alerts)):
            print('Alert[{}]: {}'.format(idx, alerts[idx]))
            print()
    else:
        print('Alert: None')

if __name__ == '__main__':
    main()
