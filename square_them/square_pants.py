"""
Magic Square Solver by imn00
Sunday - Oct 16, 2016
"""

import cookielib, urllib, urllib2, BeautifulSoup as mySoup, json

a, b, c = 2, 3, 5
url = 'http://task-00000010.itrace.systems/square.php'
white_list = 'Good job'
result = {}
next_sum = 0

cookie_jar = cookielib.CookieJar()
processor = urllib2.HTTPCookieProcessor(cookie_jar)
opener = urllib2.build_opener(processor)
urllib2.install_opener(opener)

# acquire cookie
req = urllib2.Request(url)
rsp = urllib2.urlopen(req)
soup = mySoup.BeautifulSoup(rsp.read())
x = int(soup.findAll("span", {"class": "x"})[0].string)


def execute(x):
    global next_sum, result
    x /= 3
    value = str(x + a) + ',' + str(x - a - b) + ',' + str(x + b) + ',' + str(x - a + b) + ',' + str(
        x) + ',' + str(x + a - b) + ',' + str(x - b) + ',' + str(x + a + b) + ',' + str(x - a)

    rsp = str(urllib2.urlopen(urllib2.Request(url, urllib.urlencode(dict(numbers=value)))).read())
    try:
        result = json.loads(rsp)
        next_sum = result['nextsum']
        return result['errmsg'] == white_list

    except ValueError:
        print rsp


execute(x)
while execute(next_sum):
    print result
