import requests
from bs4 import BeautifulSoup

def checkWebsite(username, website):

    keywords = ('not found', '''n't found''', '''doesn't exist''', 'not exist', '''isn't available''', 'not available')
    result = requests.get(website + username)

    code = result.status_code
    if code == 404:
        print(username + " is available on " + website)
        return
    elif code == 429:
        print("rate limited on " + website + "! try again later.")
        return

    soup = BeautifulSoup(result.content,'lxml')
    str_soup = str(soup.encode("utf-8")).lower()

    match = next((x for x in keywords if x in str_soup), False)
    if match != False:
        print(username + " is available on " + website)
    else:
        print(username + " is unavailable on " + website)




with open('websites.txt') as websitesFile:
    websites = [line.rstrip() for line in websitesFile]

with open('usernames.txt') as usernameList:
    usernames = [line.rstrip() for line in usernameList]

for i in usernames:
    for j in websites:
        checkWebsite(i, j)
    print("\n\n")



# f = open("scrapedHTML.txt", "w")
# f.write(str_soup)

# ("https://github.com/",
# "https://old.reddit.com/user/",
# "https://youtube.com/",
# "https://instagram.com/",
# "https://open.spotify.com/user/")
