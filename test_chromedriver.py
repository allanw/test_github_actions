from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time


#################
### Variables ###
#################

# Garmin Connect - Creds
webAddress = "https://sso.garmin.com/sso/login?service=https%3A%2F%2Fconnect.garmin.com%2FminExplore&webhost=olaxpw-connect00&source=https%3A%2F%2Fconnect.garmin.com%2Fen-US%2Fsignin&redirectAfterAccountLoginUrl=https%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&redirectAfterAccountCreationUrl=https%3A%2F%2Fconnect.garmin.com%2Fpost-auth%2Flogin&gauthHost=https%3A%2F%2Fsso.garmin.com%2Fsso&locale=en_US&id=gauth-widget&cssUrl=https%3A%2F%2Fstatic.garmincdn.com%2Fcom.garmin.connect%2Fui%2Fcss%2Fgauth-custom-v1.1-min.css&clientId=GarminConnect&rememberMeShown=true&rememberMeChecked=false&createAccountShown=true&openCreateAccount=false&usernameShown=false&displayNameShown=false&consumeServiceTicket=false&initialFocus=true&embedWidget=false&generateExtraServiceTicket=false"
email = 'al.whatmough@gmail.com'
password = os.environ.get("MY_SECRET")

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get(webAddress)
print("HELLO")

def clickItem(xpathstr):
    """ Click on a web element using selenium
    params
    ------
    xpathstr: string
        xPath of the web element
    """
    item = driver.find_element_by_xpath(xpathstr)
    webdriver.ActionChains(driver).click(item).perform()

time.sleep(10)

print(driver.page_source.encode("utf-8"))
    
# Enter email - press tab
webdriver.ActionChains(driver).send_keys(email).key_down(Keys.TAB).key_up(Keys.TAB).perform()
time.sleep(1)

# Enter password - press enter
webdriver.ActionChains(driver).send_keys(password).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
time.sleep(10)

driver.get('https://connect.garmin.com/modern/activity/7224500180')

time.sleep(10)

print(driver.find_element_by_xpath("""//ul[contains(@class, 'gear-names')]/li[1]""").text)
