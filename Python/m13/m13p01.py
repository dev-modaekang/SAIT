import urllib2

body = urllib2.urlopen("http://itss.biomea.com/index.html")
print body.read()
