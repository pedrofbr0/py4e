# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url < 1):
    url = 'http://py4e-data.dr-chuck.net/comments_1176852.html'
    # url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
span_tags = soup('span')

count = 0
soma = 0

for line in span_tags:
    # print(line)
    # print(int(line.contents[0]))
    count = count + 1
    soma = soma + int(line.contents[0])


print('Count ' + str(count))
print('Sum ' + str(soma))