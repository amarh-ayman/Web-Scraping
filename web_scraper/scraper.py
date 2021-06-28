import requests

from bs4 import BeautifulSoup
import json

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"

def  get_citations_needed_count(URL):
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  all_results = soup.find_all('a', title="Wikipedia:Citation needed")
  return len(all_results)


def get_citations_needed_report(URL):
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  all_results = soup.find_all('a', title="Wikipedia:Citation needed")
  reports=[]

  for result in all_results:
    res=result.parent.parent.parent
    p=res.text.strip()
  
    reports.append(p)

  # Write results to json file
  file_content = json.dumps(reports)
  with open('reports.json', 'w') as file:
      file.writelines(file_content)

  return reports

print(get_citations_needed_count(URL))
print(get_citations_needed_report(URL))
