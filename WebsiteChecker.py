import urllib.request

website = [
    'https://www.google.com', 
    'https://www.soap2day.video/',
    'https://www.rottentomatoes.com',
    ]

for link in website:
    try:
        if urllib.request.urlopen(link).getcode() == 200:
            pass
    except Exception as e:
        print('Number of websites checked: ', len(website), '\n')
        print(link, '\n')
