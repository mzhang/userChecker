from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.namegenerator.biz/fantasy-name-generator.php")
generateButton = driver.find_element_by_xpath('''//input[@value="Generate Fantasy Names"]''')

for i in range(25):
    generateButton.click()

generatedList = driver.find_element_by_xpath('''//ul[@id="textbox"]''')
items = generatedList.find_elements_by_tag_name("li")
for item in items:
    text = item.text
    print(text)

driver.quit()
