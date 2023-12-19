from urllib.request import urlopen
import urllib

def check_internet():
    try:
        urlopen('https://www.google.com', timeout=5)
        return True
        
        #Your code.. 
        #Example as sending email if there's an internet connection
        
    except urllib.error.URLError as e:
        print(e)
        return False

if check_internet():
    print("internet is connected")
else:
    print("internet is disconnected")
