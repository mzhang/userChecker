import requests
from bs4 import BeautifulSoup

def checkWebsite(username, website):
    keywords = ('not found', '''doesn't exist''', 'not exist', '''isn't available''',
                'Not Found', '''Doesn't Exist''', 'Not Exist', '''Isn't Available''',
                'Not found', '''Doesn't exist''', 'Not exist', '''Isn't available''')

    result = requests.get(website + username)
    src = result.content
    soup = BeautifulSoup(src,'lxml')

    str_soup = str(soup.encode("utf-8"))

    if any(x in str_soup for x in keywords):
        print(username + " is available on " + website)
    else:
        print(username + " is unavailable on " + website)


username = input(": ")
websites = ("https://github.com/",
            "https://old.reddit.com/user/",
            "https://youtube.com/",
            "https://twitter.com/",
            "https://instagram.com/")

for i in websites:
    checkWebsite(username, i)



# f = open("scrapedHTML.txt", "w")
# f.write(str_soup)
