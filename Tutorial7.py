#import requests

#x = requests.get('https://w3schools.com')

#print(x.text)

import requests

url ='https://w3schools.com'
response = requests.get(url)

if response.status_code == 200 :
    print(response.text)
else :
    print("404 page error")

