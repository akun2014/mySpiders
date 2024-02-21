import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)
action_chains = ActionChains(browser)


browser.get('https://www.1688.com/')

cookies = {
    "name": "foo",
    "value": "bar",
    "cookie2": "184dfba7061f4e5b280fa7aa297d2dd1",
    "t": "1ae9fd11828f2ea032bdd07b316bb7ba",
    "_tb_token_": "31ee66b141ba3",
    "_samesite_flag_": "true",
    "hng": "CN%7Czh-CN%7CCNY%7C156",
    "xlly_s": "1",
    "cna": "6ZYoHSqaBH4CATpkqlwy6mmU",
    "3PcFlag": "1705846755719",
    "sgcookie": "E100j3%2Fa1TD6flZuIet10eLTjbzagKQP7JU87BMoQoMSE4KxT98jLrDl2R6rdia%2FgEfmhXSEsi6H0dDp9DovaVQhUd7hKLSFxJzNYcugngHVjmdglmfnUONKWIli4saQdT5MA039uPZu8O2FOprbWVrNYA%3D%3D",
    "unb": "925615859",
    "uc3": "nk2=EvywP7FQwiQV&vt3=F8dD3ChAyktHJiY0L3w%3D&lg2=URm48syIIVrSKA%3D%3D&id2=WvKSnFLmRjvW",
    "csg": "7975e8c3",
    "lgc": "qiankun92",
    "cancelledSubSites": "empty",
    "cookie17": "WvKSnFLmRjvW",
    "dnk": "qiankun92",
    "skt": "a369ad1454823013",
    "existShop": "MTcwNTg0Njc1OA%3D%3D",
    "uc4": "id4=0%40WDWhqC9vaJyA7Q43SY7ndr8rDFo%3D&nk4=0%40EIOda3mS%2B%2BjZGCgPtBUz4%2B9LdvU%3D",
    "publishItemObj": "Ng%3D%3D",
    "tracknick": "qiankun92",
    "_cc_": "V32FPkk%2Fhw%3D%3D",
    "_l_g_": "Ug%3D%3D",
    "sg": "299",
    "_nk_": "qiankun92",
    "cookie1": "W8nVEKDDUzw2qf7%2F0ekUyWERKQnLanMdPCS8qKihgIA%3D",
    "mt": "ci=15_1",
    "uc1": "cookie21=URm48syIZJTgsdYlwpiWOA%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0&cookie14=UoYekEsQ1UIAtw%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false"
}

browser.add_cookie(cookies)

url = 'https://s.1688.com/selloffer/offer_search.htm?keywords=%D6%B1%B2%A5%B4%F3%B9%A6%C2%CA%B2%B9%B9%E2%B5%C6&spm=a26352.13672862.searchbox.input'

url2 = 'https://shop1460133980340.1688.com/page/offerlist.htm'

browser.get(url2)

# time.sleep(10)
#
# txt = browser.find_element(By.XPATH, '//*[@id="sm-offer-list"]/div[1]/div/div[2]/a/div').text
# print(txt)

# cookies = browser.get_cookies()
print(browser.title)

input()
