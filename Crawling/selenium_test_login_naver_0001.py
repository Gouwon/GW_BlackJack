import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os

if os.name == "nt":
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32/chromedriver.exe')
elif os.name == "posix": 
    driver = webdriver.Chrome('/Users/mac/workspace/chromedriver')  # mac or linux
else:
    print("Not supported OS")
    exit()


UserId = "jskd2938"
UserPw = "ahsgjs*3g"

driver.get("https://www.naver.com")
time.sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()
print("click big button!!")
# time.sleep(1)
driver.implicitly_wait(15) 


id = driver.find_element_by_id('id')
pw = driver.find_element_by_id('pw')


actions = ActionChains(driver)
actions.move_to_element(id)
actions.send_keys_to_element(id, UserId)
actions.pause(2)

actions.move_to_element(pw)
actions.send_keys_to_element(pw, UserPw)
actions.pause(2)

driver.find_element_by_class_name('btn_global').click()

# menu = driver.find_element_by_css_selector(".nav")
# hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

# actions = ActionChains(driver)
# actions.move_to_element(menu)
# actions.click(hidden_submenu)
# actions.perform()


# driver.implicitly_wait(5) 
# time.sleep(random.randrange(2,5)) # For bypass captcha 
# id.send_keys(UserId) 
# time.sleep(1) 
# pw.send_keys(UserPw) 
# time.sleep(randrange(2,4)) 
# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

