import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

def scrape():
 WebPage = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.290580000000034&lon=-76.60925999999995#.Xk1NjZNKhQI')

 soup = BeautifulSoup (WebPage.content, 'html.parser')   # this object loads the page content and is able to parse the html

 WeekFor = soup.find( id = 'seven-day-forecast-body')   # WeekFor finds all elemtns with ID set to seven day forecast that way i can retrieve seven day forecast

 Container = WeekFor.find_all(class_= 'tombstone-container') # Within the seven day forecast i am pretty much narrowing it down as much as i can to get all the information I want


 period_names = [item.find(class_='period-name').get_text()for item in Container]
 short_desc = [item.find( class_ ='short-desc').get_text() for item in Container]
 temp = [item.find(class_='temp').get_text() for item in Container]


 weather_data = pd.DataFrame(

    {
        'Day period': period_names,
        'outlook': short_desc,
        'Temprature': temp,

    })
 print(weather_data)

while True:

 scrape()
 time.sleep( 60 )









