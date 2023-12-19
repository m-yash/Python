import requests

url = 'https://httpstat.us/200'

res = requests.head(url)

if res.status_code == 200:
    print('site working') # 200 status_code says that the request was successful
else:
    print('not working')