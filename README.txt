Hey! 

This is a little project by github.com/Zugzhang to try and find a username for himself that isn't taken everywhere(or anywhere). 
I probably couldn't have picked this username without this little program. 

Anyway, the goal is for the .py file to read the .txt files and to see if each username exists on each website. So you can hopefully choose a username in a few minutes instead of the weeks it took me. 

This is a heuristic approach using BeautifulSoup4 - some web pages like twitter.com or twitch.tv doesn't scrape entirely using BS4. 
There exists a Selenium implementation in the 1st commit but I chose against it as it is over 10x slower. Let me know if you want me to look into finding a new solution for these websites. 