from urllib.request import *
from bs4 import BeautifulSoup as bs

response = urlopen("https://imdb.com")
htmlPage = bs(response)

imagesList = htmlPage.find_all("img")

# print(len(imagesList))

# print(imagesList[0]['src'])

for i in range(len(imagesList)):
    image_link = imagesList[i]['src']
    file_extension = image_link[-3:]
    if file_extension != "png":
        file_name = f"{i+1}.{file_extension}"
        urlretrieve(image_link, file_name)