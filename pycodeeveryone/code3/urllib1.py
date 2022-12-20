import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for x in fhand:
    print(x.decode().strip())
