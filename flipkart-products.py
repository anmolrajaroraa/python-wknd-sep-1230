from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

response = urlopen("https://www.flipkart.com/search?q=electronics&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off") #http request
# print(response)
htmlPage = bs(response)
# print(htmlPage)

#For one product
productNameBlock = htmlPage.find('a','_2cLu-l')
productName = productNameBlock.text
print(productName)

#For all products
productsList = htmlPage.find_all('a','_2cLu-l')
print(len(productsList))

pricesList = htmlPage.find_all('div', '_1vC4OE')
print(len(pricesList))

#For printing names
# for productNameBlock in productsList:
#     productName = productNameBlock.text
#     print(productName )

#For printing names with prices
for i in range(40):
    productName = productsList[i].text
    price = pricesList[i].text
    print(f"{productName.ljust(60)} -> {price}") #left-justified - creates an empty string of 60 characters and then puts my string on the left side and rest of the characters are printed as empty spaces