Hey! 



This is a little project by github.com/Zugzhang to try and find a username for himself that isn't taken everywhere(or anywhere). 
I probably couldn't have picked this username without this little program. 

This is a heuristic approach using BeautifulSoup4 - some web pages like twitter.com or twitch.tv doesn't scrape entirely using BS4. 
There exists a Selenium implementation in the 1st commit but I chose against it as it is over 10x slower. Let me know if you want me to look into finding a new solution for these websites. 



Anyway, the goal is for the .py file to read usernames.txt and websites.txt and to see if each username exists on each website. So you can hopefully choose a username in a few minutes instead of the weeks it took me. 

Also, I ended up making scrapeUsernames.py, which outputs a list of 25 randomly generated and cool-sounding names... and puts it all into usernames.txt, which the soupUsernameCheck.py will check availablity for you.

There's also a .bat to run them both .py files in order! 

The chance of someone seeing this is next to none, so if you happen to have defied fate and are reading this, please let me know where and how I can improve this as I am very evidently new to this! 
