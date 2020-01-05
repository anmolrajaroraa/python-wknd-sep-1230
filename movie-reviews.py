from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

movie_name = input("Which movie do you want to see details for: ")
page_link = f"https://www.imdb.com/find?q={movie_name}&s=tt&ref_=fn_al_tt_mr"
# print(page_link)
page_link = page_link.replace(" ", "+")
# print(page_link)
response = urlopen(page_link)
htmlPage = bs(response)
htmlPage.find()



movie_choice = input("Which one?")
movie_choice = movie_choice - 1
td = movies_list[movie_choice]
link_to_next_page = td.find('a')
new_link = link_to_next_page['href']