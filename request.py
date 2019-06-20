# import requests

# response = requests.get('http://www.baidu.com')
# print(response.text)
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("www.taobao.com")