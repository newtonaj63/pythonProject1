# To run this, download the BeautifulSoup zip file
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import ssl
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
repeat = int(input('number of times to repeat'))
position = int(input('Position in list'))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
for i in range(repeat):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link_list, name_list = [], []
    for tag in tags:
        link_list.append(tag.get('href', None))
        name_list.append(tag.text)

    print(link_list[position - 1])
    print(name_list[position - 1])
    url = link_list[position - 1]
