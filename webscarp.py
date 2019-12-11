import requests
from bs4 import BeautifulSoup
t=input("enter the job you want to search\n")
n=input("enter the keyword regarding field\n")
url="https://www.monster.com/jobs/search/?q="+t+"&where=INDIA"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
result=soup.find(id='SearchResults')
##print(page)
##print(result.prettify())
job_elems = result.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    time = job_elem.find('time')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print(time.text.strip())
    print()
    
python_jobs = result.find_all('h2',string=lambda text: '+n+' in text.lower())
print(len(python_jobs))
print(python_jobs)
#data_analyst=result.find_all('h2',string='Data Analyst')

