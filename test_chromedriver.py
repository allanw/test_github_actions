from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time


#################
### Variables ###
#################

# Garmin Connect - Creds
webAddress = "https://connect.garmin.com/"
email = 'al.whatmough@gmail.com'
password = os.environ.get("MY_SECRET")

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
driver = webdriver.Chrome(options=chrome_options)
driver.get(webAddress)
print("HELLO")
print(driver.page_source.encode("utf-8"))

def clickItem(xpathstr):
    """ Click on a web element using selenium
    params
    ------
    xpathstr: string
        xPath of the web element
    """
    item = driver.find_element_by_xpath(xpathstr)
    webdriver.ActionChains(driver).click(item).perform()

# Click login button
clickItem("""//*[@id="___gatsby"]/div/div/header/nav/ul/li[4]/a/button""")
time.sleep(10)

# Enter email - press tab
webdriver.ActionChains(driver).send_keys(email).key_down(Keys.TAB).key_up(Keys.TAB).perform()
time.sleep(1)

# Enter password - press enter
webdriver.ActionChains(driver).send_keys(password).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
time.sleep(10)

driver.get('https://connect.garmin.com/modern/activity/7224500180')

time.sleep(10)

print(driver.find_element_by_xpath("""//ul[contains(@class, 'gear-names')]/li[1]""").text)
