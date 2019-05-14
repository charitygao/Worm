#模拟浏览器操作
from selenium import webdriver                              #导入库
useremail = input('useremail:')
password = input('password:')
driver = webdriver.PhantomJS()                              #指定浏览器
driver.get('https://douban.com/')                           #请求url
driver.implicitly_wait(10)                                   #隐式等待10s
driver.find_element_by_id('username').clear()             #清除输入框数据
driver.find_element_by_id('username').send_keys(useremail)  #输入账号
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_key(password)
driver.find_element_by_class_name('btn btn-account').click()      #单击登入框
print(driver.page_source)                                   #打印网页源代码