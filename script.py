from selenium import webdriver
import time

########################
#
# 官方已经开通自动填写功能了
# 只有所在区域没有自动填写
# 所以此脚本为填补空白
#
########################


### 配置区 ###
config_sheng = 1 #省的编号
config_shi = 1 #市的编号
config_xian = 1 #县的编号
username = 1 #账号
password = 1 #密码
drivername = "./chromedriver" #驱动文件路径
howtime = 19 #几点
phone = 13676763333 #联系电话,如果你的手机号自动填写了 请在下面注释提交手机的代码

speed_for_page = 20 #每一页加载的时间
speed_for_load = 10 #每一个选项加载的时间
url = 'https://域名/mobile/index.html' #请自己填写域名
#############




### 代码区 ###
def run():
    browser = webdriver.Chrome(executable_path=drivername)
    browser.get(url) 
    time.sleep(speed_for_page)
    browser.find_element_by_name("username").click()
    browser.find_element_by_name("username").clear()
    browser.find_element_by_name("username").send_keys(str(username))
    browser.find_element_by_name("password").click()
    browser.find_element_by_name("password").clear()
    browser.find_element_by_name("password").send_keys(str(password))
    browser.find_element_by_xpath("//div[@id='root']/div/div[2]/button").click()
    time.sleep(speed_for_page)
    browser.execute_script('document.getElementsByClassName("grid-item-wrapper")[0].click()')
    time.sleep(speed_for_page)


    #电话 -> 注释下面一句语句可以防止设置电话
    browser.find_elements_by_class_name("weui-textarea")[3].send_keys(str(phone))
    #browser.execute_script('document.getElementsByClassName("weui-textarea")[3].value=' + str(phone))
    time.sleep(speed_for_load)

    #省
    browser.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/div/div[16]/div[2]").click()
    time.sleep(speed_for_load)
    browser.execute_script('document.getElementsByClassName("weui-check__label")[' +  str(config_sheng)  + '].click()')
    time.sleep(speed_for_load)

    #市
    browser.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/div/div[18]/div[2]").click()
    time.sleep(speed_for_load)
    browser.execute_script('document.getElementsByClassName("weui-check__label")[' +  str(config_shi)  + '].click()')
    time.sleep(speed_for_load)

    #县
    browser.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/div/div[20]/div[2]").click()
    time.sleep(speed_for_load)
    browser.execute_script('document.getElementsByClassName("weui-check__label")[' +  str(config_xian)  + '].click()')
    time.sleep(speed_for_load)


    #提交
    browser.execute_script('document.getElementsByClassName("weui-btn")[0].click()')
    time.sleep(speed_for_load)

while(True):
     hour = time.localtime().tm_hour
     if hour == howtime:
         print("***任务开始执行***")
         run()
         print("***任务执行完毕***")
         print("现在时间:"+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
         time.sleep(7200)
     time.sleep(1800)
#############