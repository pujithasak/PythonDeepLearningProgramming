import requests
from bs4 import BeautifulSoup

links = []

# The web page content is assigned to wikiPage variable by using request
wikiPage = requests.get("https://en.wikipedia.org/wiki/Deep_learning")

# By using beautiful soup parsing the page content
data = BeautifulSoup(wikiPage.content, "html.parser")
print("Title of the web page is : ", data.title.string)


# By using For loop all the links in page are append to the list
for link in data.find_all('a'):
    links.append(link.get('href'))
print("links in the page are :" + str(links))

# writing the output to the file
with open('OutputFile.txt', 'w') as file:
    for link in links:
        file.write('%s\n' % link)
