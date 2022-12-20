from urllib import request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1658027.xml'
print("Retrieving", url)
xml = request.urlopen(url)
data = xml.read()
print("Retrieved", len(data), "characters")

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
icount = len(results)
isum = 0

for result in results:
    isum += int(result.find('count').text)


