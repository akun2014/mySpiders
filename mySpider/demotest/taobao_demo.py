import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)
action_chains = ActionChains(browser)

url = 'https://shop1460133980340.1688.com/page/offerlist.htm?spm=a2615.2177701.wp_pc_common_topnav.0'

browser.get(url)

time.sleep(3)

browser.find_element(By.XPATH, '//*[@id="fm-login-id"]').send_keys('qiankun92')
browser.find_element(By.XPATH, '//*[@id="fm-login-password"]').send_keys('Taobao@176219')

time.sleep(3)

slider = browser.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
if slider.is_displayed():
    action_chains.click_and_hold(slider)
    action_chains.move_by_offset(345, 0)
    action_chains.perform()
    time.sleep(0.5)
    # action_chains.release().perform()

browser.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/button').click()

input()
