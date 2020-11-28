# pip install selenium
# download chrome driver from https://chromedriver.chromium.org/downloads
# extract chromedriver in any folder from c drive or create new dir for webdrivers
# copy full path of the file and pass it as keyword argument in webdriver.chrome method
# change the time.sleep methods argument according to the response time of instagram

from selenium import webdriver
from cred import username, password, recovery_code
import time

time.sleep(2.0)

msg = '''Hello...!!!
This Is My New Instagram Bot For Sending Message For Source Code DM Me....'''
chrome_browser = webdriver.Chrome(
    executable_path=r"paste full path with extenssion")
# for example
# chrome_browser = webdriver.Chrome(
#     executable_path=r"C:\Users\Abhi-Lenovo\Webdrivers\chromedriver.exe")


def start_service():
    '''
        This method will open new chrome window in maximized state 
        it will launch the instagram website
    '''
    chrome_browser.maximize_window()
    chrome_browser.get("https://www.instagram.com/")
    time.sleep(2.0)


def login():
    '''
        This method will handle all work related with username and password
    '''
    chrome_browser.find_element_by_xpath(
        '//input[@class="_2hvTZ pexuQ zyHYP"]').send_keys(username)
    chrome_browser.find_element_by_xpath(
        '//input[@name="password"]').send_keys(password)
    time.sleep(0.5)
    chrome_browser.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(6.0)


def send_message():
    '''
        This method will find element with the profile name 
        passed in the find element method as below

    '''
    chrome_browser.find_element_by_xpath('//div[@class="cmbtv"]').click()
    time.sleep(4.0)
    chrome_browser.find_element_by_xpath(
        '//button[@class="aOOlW   HoLwm "]').click()
    time.sleep(2.0)
    chrome_browser.find_element_by_xpath('//a[@class="xWeGp"]').click()
    time.sleep(6.0)

    chrome_browser.find_element_by_xpath(
        '//div[text()="username here of the receiver"]').click()
    # if username is ab_g_r_a_p_h_y then following code can used as ref
    # chrome_browser.find_element_by_xpath(
    #     '//div[text()="ab_g_r_a_p_h_y"]').click()

    time.sleep(3.0)
    chrome_browser.find_element_by_xpath(
        '//textarea[@placeholder="Message..."]').send_keys(msg)
    time.sleep(2.0)
    chrome_browser.find_element_by_xpath('//button[text()="Send"]').click()


# use this code if user activated two step varification
'''
def verification():
    chrome_browser.find_element_by_xpath(
        '//input[@name="verificationCode"]').send_keys(recovery_code)
    time.sleep(0.5)
    chrome_browser.find_element_by_xpath('//button[@type="button"]').click()
    time.sleep(6.0)
'''


def main():
    start_service()
    login()
    send_message()


if __name__ == "__main__":
    main()
