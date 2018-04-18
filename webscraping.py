import urllib.request
from bs4 import BeautifulSoup # need to install library first
url = 'https://finance.yahoo.com/quote/FB?p=FB'

headers ={'Header: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

req = urllib.request.Request(url, headers=headers)

resp = urllib.request.urlopen(req)

html = resp.read()

soup = BeautifulSoup(html, 'html.parser')

tagged_values = soup.find_all("td", {'class''Ta(end) Fw(b)'})
print(tagged_values)

values = [x.get_text() for x in tagged_values]

for value in values:
    print(value)

    print('\n')