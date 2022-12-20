import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tree = ET.urllib.parse('http://py4e-data.dr-chuck.net/comments_42.xml','xmlpharser')





