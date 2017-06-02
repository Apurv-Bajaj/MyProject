import urllib2
prime="http://www.mathematical.com/primes0to1000k.html"
page=urllib2.urlopen(prime)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page)
print soup.prettify()
