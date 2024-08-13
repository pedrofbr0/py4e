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

url = input('Enter URL: ')

if len(url) < 1: url = '  http://py4e-data.dr-chuck.net/known_by_Jamie.html'

count = input('Enter Count: ')
if len(count) < 1: count = 7

position = input('Enter Position: ')
if len(position) < 1: position = 18

last_name = ''

while count > 0:
    print('Retrieving: ', url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor ('a') tags
    anchor_tags = soup('a')
    
    new_url = anchor_tags[position-1].get('href', None)
    new_name = anchor_tags[position-1].contents[0]
    last_name = new_name
    # print(new_name)
    
    count = count - 1
    url = new_url

#    for line in anchor_tags:
#        print(line)
#        print(line.contents[0])
#        print(line.get('href', None))
print('Last Name: ', last_name)
