#made by 湉曦tx
from selenium import webdriver
import time
# 导入模块，等下用
class zafu_infos:
    def __init__(self):#定义初始化函数
        url = "http://10.152.250.2/srun_portal_pc?ac_id=1&theme=zafu"#网络登录的地址
        self.url = url
        self.browser = webdriver.Chrome('C:\Program Files\Python39\chromedriver.exe')#加入浏览器的驱动如果是google或火狐要改

    def login(self):#登录函数
        self.browser.get(self.url)#浏览器驱动打开网站
        zafu_user = self.browser.find_element_by_xpath('//*[@id="username"]')#用户名的输入框
        zafu_user.send_keys('账号+服务商')#用户名+服务商移动用@cmcc电信用@chinanet 例子:123456789012@cmcc
        zafu_password = self.browser.find_element_by_xpath('//*[@id="password"]')#密码的输入框
        zafu_password.send_keys('密码')#密码
        submit = self.browser.find_element_by_xpath('//*[@id="login"]')#登录的按钮
        submit.click()#点击登录按钮
        time.sleep(0.5)#等待0.5秒，没等待无法登录



zafu_infos().login()#执行登录
exit()#退出python
