from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

driver.get("https://www.namegenerator.biz/fantasy-name-generator.php")
generateButton = driver.find_element_by_xpath('''//input[@value="Generate Fantasy Names"]''')

for i in range(25):
    generateButton.click()

generatedList = driver.find_element_by_xpath('''//ul[@id="textbox"]''')
items = generatedList.find_elements_by_tag_name("li")

with open("usernames.txt", 'w') as f:
    output = []

    for item in items:
        output = item.text
        f.write(output + "\n")

    f.close()

driver.quit()
