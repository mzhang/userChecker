import requests
from bs4 import BeautifulSoup

def isUsernameAvailable(username, website):

    keywords = ('not found', '''n't found''', '''doesn't exist''', 'not exist', '''isn't available''', 'not available')
    result = requests.get(website + username)

    code = result.status_code
    if code == 404:
        return True
    elif code == 429:
        raise Exception()

    soup = BeautifulSoup(result.content,'lxml')
    str_soup = str(soup.encode("utf-8")).lower()

    match = next((x for x in keywords if x in str_soup), False)
    if match != False:
        return True
    else:
        return False

with open('websites.txt') as websitesFile:
    websites = [line.rstrip() for line in websitesFile]
    websitesFile.close()

with open('usernames.txt') as usernamesFile:
    usernames = [line.rstrip() for line in usernamesFile]
    usernamesFile.close()

for i in usernames:
    for j in websites:
        try:
            print(i + " is available on " + j) if isUsernameAvailable(i, j) else print(i + " is unavailable on " + j)
        except:
            print("Rate limited on " + j + "! Try again later.")
    print("\n\n")
