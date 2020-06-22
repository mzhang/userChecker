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
    websitesFile.close()

with open('usernames.txt') as usernamesFile:
    usernames = [line.rstrip() for line in usernamesFile]
    usernamesFile.close()

for i in usernames:
    for j in websites:
        checkWebsite(i, j)
    print("\n\n")
