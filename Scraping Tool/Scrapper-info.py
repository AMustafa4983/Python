import pandas as pd 
import requests
from bs4 import BeautifulSoup

df = pd.read_csv('Links.csv')

names = []
exps = []
emails = []

for i in df['links']:
    print('The Link is: ',i)
    request = requests.get(i)
    soup = BeautifulSoup(request.content, 'html5lib')
    try:
        name = soup.find('h1',{'class':'hero-content__title'}).text
    except:
        print('No Name!')
        
    try:
        exp = soup.find('td',{'style':'padding-bottom:10px;'}).find('strong').text
    except:
        print('No EXP!')
        exp = ''

    try:
        refs = soup.find('div',{'class':'col-md-4 col-bg-gray small'}).find_all('a')
        for a in refs:
            if '@' in a.text:
                email = a.text
    except:
        print('No Email!')
        continue
    if email not in emails:
        names.append(name)
        exps.append(exp)
        emails.append(email)
        
        print('---- driver ----')
        print(f'Fname:{name}, Email: {email}\n')
    else:
        print('record removed!')

df2 = pd.DataFrame({'names':names, 'exp':exps,'emails':emails})
df2.to_csv(f"Emails.csv")
print('CSV Done!')