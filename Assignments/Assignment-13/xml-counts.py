import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    # address = 'http://py4e-data.dr-chuck.net/comments_1176854.xml'
    if len(address) < 1: adress = 'http://py4e-data.dr-chuck.net/comments_1176854.xml'

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    # print('serviceurl', serviceurl)
    # url = serviceurl + urllib.parse.urlencode(parms)
    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    # print('uh', uh)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    # print(data.decode())
    tree = ET.fromstring(data)
    # print('Tree', tree)
    # tree = ET.parse(address)
    # count = len(tree)
    # print('Count: ', count)
    
    counts = tree.findall('.//count')
    
    soma = 0
    
    for count in counts:
        soma = soma + int(count.text)
    
    print('Counts: ', len(counts))

    print('Sum: ', soma)