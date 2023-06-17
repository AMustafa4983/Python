import pandas as pd 
import requests
from bs4 import BeautifulSoup


links = []

url = ' Your_Link'
for i in range(0,220):
    print('for Page: ',i)
    request = requests.get(f'{url}/?page={i}')
    soup = BeautifulSoup(request.content, 'html5lib')
    try:
        entities = soup.find_all('div',{'class':'col-xs-8'})
        for entity in entities:
            link = entity.find('p').find('a')
            link = url +link['href']

            if link not in links:
                links.append(link)
                print('---- driver ----')
                print(f'Link: {link}\n')
            else:
                print('record removed!')
    except:
        print('No Link!')


df2 = pd.DataFrame({'links':links})
df2.to_csv(f"Links.csv")
print('CSV Saved!')