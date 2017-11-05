import requests
import csv
from BeautifulSoup import BeautifulSoup

url = "http://apps2.whatcomcounty.us/onlineapps/jailrosters/bookings/booking.jsp"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

table = soup.find('table', attrs={"xmlns":"http://www.w3.org/1991/xhtml"})
print(table.prettify())

with open("jailroster.csv", "w") as jailfile:
	writer = csv.writer(jailfile, quoting=csv.QUOTE_ALL)

	for row in table.findAll('tr'):
		# pretend_variable = ["bla", "bla"]
		# print(row.text)
		# writer.writerow([row.text])
		rowlist = []
		for line in row.findAll('td'):
			rowlist.append(line.text)
			# print(rowlist)
		writer.writerow(rowlist)




# print(soup.prettify())