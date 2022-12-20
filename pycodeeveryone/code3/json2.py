import json
from urllib.request import urlopen

url = input("Enter the url")
print("Retreivng Url:" + url)
response = urlopen(url)
data_json = json.loads(response.read())
total = 0
for people in data_json["comments"]:
    x = int(people["count"])
    total = x + total
print()
print(len(url))
print(total)
