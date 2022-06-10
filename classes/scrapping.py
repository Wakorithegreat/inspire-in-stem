

import requests
from bs4 import BeautifulSoup as bs

user_name = "Maddie"
url = "https://git.com/" +user_name
results = requests.get(url)

soup = bs(results.content,"html.parser")
profile_pic = soup.find('img',{'alt':'Avatar'})
print(profile_pic)