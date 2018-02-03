from selenium import webdriver
import time
from lxml import etree
import urllib.request
import traceback

def getPages():
    # 替换成你的sitemap
    url = "https://sparkera.net/sitemap.xml"
    webPage=urllib.request.urlopen(url)
    html = webPage.read()
    html = etree.HTML(html)
    script = html.xpath("//loc/text()")
    print(script)
    print(type(script))
    return script

# 替换成你的chrome驱动的路径
driver = webdriver.Chrome(executable_path=r"D:\chromeDriver\chromedriver.exe")
driver.get("https://github.com/login")

# 替换成你的账号密码
username = 'hackeryard'
password = 'xxxxxx'
driver.find_element_by_id("login_field").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_name("commit").click()

# click init button in pages from the sitemap.xml
urls = getPages()
flag = 0
for url in urls:
    driver.get(url)
    if flag == 0:
        driver.find_element_by_xpath("//a[@class='gitment-editor-login-link']").click()
        flag = 1

    time.sleep(5)
    try:
        driver.find_element_by_xpath("//button[@class='gitment-comments-init-btn']").click()
        # wait for init done
        time.sleep(5)
        print("已初始化")
    except:
        print("无需初始化") 
