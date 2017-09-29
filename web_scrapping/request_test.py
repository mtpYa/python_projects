import urllib.request
from urllib.error import HTTPError, URLError
# import urllib.parse

url = 'http://google.com'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
# values = {
#     'name': 'user',
#     'surname': 'home'
# }
headers = {
    'User-Agent': user_agent,
    'Content-Length': 0
}

# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
req = urllib.request.Request(url, None, headers)
try:
    with urllib.request.urlopen(req) as response:
        print(response.geturl())
        print(response.info())
except HTTPError as err:
    print('Server error')
    print(err.code)
except URLError as err:
    print('Error sending request')
    print(err.reason)
