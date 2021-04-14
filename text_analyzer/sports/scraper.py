from bs4.element import TemplateString
import requests
from bs4 import BeautifulSoup
from requests.api import head

team_types = set()
scrape_this = r"https://en.wikipedia.org/wiki/Men%27s_FIH_Hockey_World_Cup#Team_appearances"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/65.0',
}
content = requests.get(scrape_this, headers=headers).text
# print(content)
soup = BeautifulSoup(content, "lxml")

# getting the first table on the page
team_table = soup.find_all("table", {"class": "wikitable"})[3]
# print(team_table)
# getting headers of the table
headers = [tr for tr in team_table.find_all('tr')]

print("Headers:", headers[0].find('th').contents[0].strip())
# exit(1)
# num_columns = len(headers)
nationalities = []
for row in team_table.find_all('tr')[1:-1]:
    country = row.find_all('td')[0].contents[1].contents
    # nationality = row.find_all('td')[1].contents[0].strip()
    print(country)
    nationalities.append(country)
    # teams.append(team)

with open('raw_data/hockey_teams.txt', 'a') as f:
    for c in nationalities:
        f.write(c[0]+"\n")
