from urllib2 import Request, urlopen, URLError

request = Request('https://www.google.com/?gws_rd=ssl#q=hat')

try:
    response = urlopen(request)
    responseB = response.read()
    
    print responseB[1:3000]
except URLError, e:
    print 'Got an error: ', e