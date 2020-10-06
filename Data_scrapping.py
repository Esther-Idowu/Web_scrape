from bs4 import BeautifulSoup
import requests
import re

header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
BaseUrl = "https://www.businesslist.com.ng"
url = BaseUrl + "/category/interior-design/13/city:lagos"
r = requests.get(url, headers=header, verify=False)

page_soup = BeautifulSoup(r.content, "html.parser")
containers = page_soup.findAll('div', class_='company with_img g_0')
containerss = page_soup.findAll('div', class_='company g_0')

filename = "Interior_D13.csv"
f = open(filename, "w")
f.write("Company Name,Year\n")

def getCompanyDetails(link):
	r = requests.get(link, headers=header, verify=False)
	page_soup = BeautifulSoup(r.content, "html.parser")
	name = page_soup.find('b', id='company_name').get_text()
	cDet = page_soup.find("div", class_="cmp_details_in")
	cYear = re.findall(r"\s(\d{4})E", cDet.get_text())
	year = cYear[0] if len(cYear) else ''
	print(name + " " + year)
	f.write("\"" + name + "\",\"" + year + "\"\n")

for container in containerss:
	brand = container.a["title"]
	link = BaseUrl + container.a["href"]
	getCompanyDetails(link)

for container in containers:
	brand = container.a["title"]
	link = BaseUrl + container.a["href"]
	getCompanyDetails(link)

