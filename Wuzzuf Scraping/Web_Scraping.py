import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
titles = []
companies = []
location = []
work = []
links = []
req = []
lists = [titles,companies,location,work,links,req]



url = "https://wuzzuf.net/search/jobs/?q=data+scientist&a=hpb"
result = requests.get(url)

src = result.content 
soup = BeautifulSoup(src,"lxml")

job_titles = soup.find_all("h2",{"class":"css-m604qf"})
job_companies = soup.find_all("a",{"class":"css-17s97q8"})
job_location = soup.find_all("span",{"class":"css-5wys0k"})
work_type  = soup.find_all("span",{"class":"css-1ve4b75 ex6kyvk0"})



for i in range(len(job_titles)):

    titles.append(job_titles[i].text)
    location.append(job_location[i].text)
    companies.append(job_companies[i].text)
    work.append(work_type[i].text)
    links.append(job_titles[i].find("a").attrs['href'])


for link in links :
    result = requests.get(link)

    src = result.content 
    soup = BeautifulSoup(src,"lxml")
    

    requirements = soup.find("div",{"class":"css-1t5f0fr"}).ul
    req_text = ""
    for li in requirements.find_all("li"):
        req_text += li.text +("| ")
    req_text = req_text[:-2]
    req.append(req_text)

unzip_lists = zip_longest(*lists)
with open(r"C:\Users\HI-TECH\Desktop\Wuzzuf\jobs.csv", "w" , encoding="UTF-8") as myfile:
    wr = csv.writer(myfile)

    wr.writerow(["title","location","Company","Work_type","Link","Requirements"])
    wr.writerows(unzip_lists)