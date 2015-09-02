import urllib.request

response = urllib.request.urlopen('http://placekitten.com/g/500/900')
html = response.read()
print(html)

with open('cat_500_500.jpg', 'wb') as f:
    f.write(html)
