from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

response = urlopen("https://www.amazon.in/dp/B0791YHVMK?pf_rd_p=bc85a87d-e7ce-4696-8858-261c3fc4538f&pf_rd_r=BA9KXMXN2B783N05R2EM") 

htmlPage = bs(response)

productNameBlock = htmlPage.find("span", id="productTitle")
productName = productNameBlock.text.strip()
priceBlock = htmlPage.find("span", id="priceblock_ourprice")
price = priceBlock.text
print(productName,price)

blockContainingPageLink = htmlPage.find("a", "a-link-emphasis a-text-bold")
# print(blockContainingPageLink)
#href - hyper reference
linkToNextPage = blockContainingPageLink['href']
# print(linkToNextPage)

completeLink = "https://www.amazon.in" + linkToNextPage
print(completeLink)

response = urlopen(completeLink)
reviewsPage = bs(response)
reviewsList = reviewsPage.find_all("a", "a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold")
# for review in reviewsList:
#     print(review.text)

for i in range(len(reviewsList)):
    print(i + 1,reviewsList[i].text)