import urllib.request
import urllib.error

req = urllib.request.Request("http://www.xxoo.fish.com")
try:
    urllib.request.urlopen(req)

except urllib.error.URLError as e:
    print(e.reason)
    
