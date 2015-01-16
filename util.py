import urllib2

def readURL(url):
    a = urllib2.urlopen(url)
    return a.read()
