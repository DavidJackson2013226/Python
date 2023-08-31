from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url='https://www.accuweather.com/en/in/surat/202441/daily-weather-forecast/202441'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
r=requests.get(url, headers=headers)
soup1 = BeautifulSoup(r.content, 'html.parser') 
print(soup1.prettify())
   
data=[]

for mainrow in soup1.findAll('div', attrs = {'class':['page-column-1']}):
    for mainrow1 in mainrow.findAll('div', attrs = {'class':['content-module non-ad','content-module non-ad bottom-forecast']}):
        for row in mainrow1.findAll('a', attrs = {'class':['forecast-list-card forecast-card','today']}):
            row1 = row.find('div', attrs = {'class':'date'})
            day = row1.find('p', attrs = {'class':'dow'}).get_text().strip()
            date = row1.find('p', attrs = {'class':'sub'}).get_text().strip()
            
            row1 = row.find('div', attrs = {'class':'temps'})
            high = row1.find('span', attrs = {'class':'high'}).get_text().strip()
            low = row1.find('span', attrs = {'class':'low'}).get_text().strip().split(" ")[1]
            
            phrase = row.find('span', attrs = {'class':'phrase'}).get_text().strip()
            
            one = {} 
            one['day']=day
            one['date']=date
            one['high']=high
            one['low']=low
            one['phrase']=phrase
            
            data.append(one)

df=pd.DataFrame(data)
print(df)

