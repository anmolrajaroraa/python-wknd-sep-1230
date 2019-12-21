from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

response = urlopen("https://www.amazon.in/Ferrero-Rocher-Chocolate-Pcs-200/dp/B07PF8J2LY/ref=sr_1_5?crid=39NE30C1ULXB8&keywords=ferrorocher+chocolates&qid=1576918526&sprefix=ferr%2Caps%2C298&sr=8-5") #http request
# print(response)
htmlPage = bs(response) #source code
# print(type(htmlPage))
productNameBlock = htmlPage.find('span', id='productTitle')
# print(productNameBlock)
productName = productNameBlock.text
print(type(productName))
productName = productName.strip()
print(productName)








# a = "            Ferrero Rochers         "    #string is immutable (cannot be changed)
# # a = a.replace("  ", "")
# # print(a)
# print(a.strip())
# print(dir(str))