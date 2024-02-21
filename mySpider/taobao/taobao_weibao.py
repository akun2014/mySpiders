import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 定义一个taobao类
class taobao_infos:

    # 对象初始化
    def __init__(self):
        url = 'https://s.taobao.com/search'
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium

        self.browser = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.browser, 10)  # 超时时长为10s

    # 登录淘宝
    def login(self):
        # 打开网页
        # self.browser.get('https://login.taobao.com/')
        self.browser.get(self.url)

        c_dict = get_cookies()
        print(c_dict)
        # 添加cookies

        self.browser.add_cookie(cookie_dict=c_dict)

        self.browser.refresh()

    # 等待 登录按钮 出现.
    # 等待 微博登录选项 出现
    # weibo_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#login-form > div.login-blocks.sns-login-links > a.weibo-login')))
    # weibo_login.click()

    # 等待 微博账号 出现
    # pl_login_logged > div > div:nth-child(2) > div > input
        weibo_user = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="q"]')))
        weibo_user.send_keys(weibo_username)

    # 等待 微博密码 出现
    # weibo_pwd = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))
    # weibo_pwd.send_keys(weibo_password)

    # 等待 登录按钮 出现
        submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button')))
        submit.click()
        time.sleep(5)

    # 直到获取到淘宝会员昵称才能确定是登录成功
        taobao_name = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                  '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[2]/div[3]/div/div[1]/a/div/div[1]/div[1]/img')))
    # 输出淘宝昵称
        print(taobao_name.get_attribute('src'))


def get_cookies():
    cookies_str = 'cookie2=184dfba7061f4e5b280fa7aa297d2dd1; t=1ae9fd11828f2ea032bdd07b316bb7ba; _tb_token_=31ee66b141ba3; _samesite_flag_=true; hng=CN%7Czh-CN%7CCNY%7C156; xlly_s=1; cna=6ZYoHSqaBH4CATpkqlwy6mmU; 3PcFlag=1705846755719; sgcookie=E100j3%2Fa1TD6flZuIet10eLTjbzagKQP7JU87BMoQoMSE4KxT98jLrDl2R6rdia%2FgEfmhXSEsi6H0dDp9DovaVQhUd7hKLSFxJzNYcugngHVjmdglmfnUONKWIli4saQdT5MA039uPZu8O2FOprbWVrNYA%3D%3D; unb=925615859; uc3=nk2=EvywP7FQwiQV&vt3=F8dD3ChAyktHJiY0L3w%3D&lg2=URm48syIIVrSKA%3D%3D&id2=WvKSnFLmRjvW; csg=7975e8c3; lgc=qiankun92; cancelledSubSites=empty; cookie17=WvKSnFLmRjvW; dnk=qiankun92; skt=a369ad1454823013; existShop=MTcwNTg0Njc1OA%3D%3D; uc4=id4=0%40WDWhqC9vaJyA7Q43SY7ndr8rDFo%3D&nk4=0%40EIOda3mS%2B%2BjZGCgPtBUz4%2B9LdvU%3D; publishItemObj=Ng%3D%3D; tracknick=qiankun92; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=299; _nk_=qiankun92; cookie1=W8nVEKDDUzw2qf7%2F0ekUyWERKQnLanMdPCS8qKihgIA%3D; mt=ci=15_1; uc1=cookie21=URm48syIZJTgsdYlwpiWOA%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0&cookie14=UoYekEsQ1UIAtw%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false'
    cookies = {}
    for item in cookies_str.split('; '):
        key, value = item.split('=', maxsplit=1)
        cookies[key] = value
    return cookies


# 使用教程：
# 1.下载chrome浏览器:https://www.google.com/chrome/
# 2.查看chrome浏览器的版本号，下载对应版本号的chromedriver驱动:http://chromedriver.storage.googleapis.com/index.html
# 3.填写chromedriver的绝对路径
# 4.执行命令pip install selenium
# 5.打开https://account.weibo.com/set/bindsns/bindtaobao并通过微博绑定淘宝账号密码

if __name__ == "__main__":
    chromedriver_path = "/Users/bird/Desktop/chromedriver.exe"  # 改成你的chromedriver的完整路径地址
    weibo_username = "ipad"  # 改成你的微博账号
    weibo_password = "password"  # 改成你的微博密码

    a = taobao_infos()
    a.login()  # 登录
