import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) <1: url = 'http://py4e-data.dr-chuck.net/comments_1176855.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
# print('uh', uh)

data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)

# print(info)

print('Count: ', len(info['comments']))

soma = 0

for person in info['comments']:
    soma = soma + int(person['count'])

print('Sum: ', soma)