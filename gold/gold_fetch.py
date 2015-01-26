import urllib.request

BASE = 'http://www.usagold.com/reference/prices/%d.html'

START = 1973
END = 2014

for year in range(START, END):
    print(year)
    remote = urllib.request.urlopen(BASE % year)
    with open('gold/%d.html' % year, 'wt', encoding='utf8') as local:
        local.write(remote.read().decode('iso8859-1'))

