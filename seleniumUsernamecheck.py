from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def testGithub(username):
    driver.get("http://www.github.com/" + username)

    try:
        content = driver.find_element_by_xpath('''//img[@alt="404 “This is not the web page you are looking for”"]''')
    except:
        print(username + " is unavailable on Github")
    else:
        print(username + " is available on Github")

def testReddit(username):
    driver.get("http://www.reddit.com/u/" + username)

    try:
        content = driver.find_element_by_xpath("//*[contains(text(), 'nobody on Reddit goes by that name')]")
    except:
        print(username + " is unavailable on Reddit")
    else:
        print(username + " is available on Reddit")

def testYoutube(username):
    driver.get("http://www.youtube.com/" + username)

    try:
        content = driver.find_element_by_xpath('''//iframe[@src="/error?src=404&ifr=1&error="]''')
    except:
        print(username + " is unavailable on Youtube")
    else:
        print(username + " is available on Youtube")



options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

username = input(": ")

testGithub(username)
testReddit(username)
testYoutube(username)
driver.quit()
exit()
