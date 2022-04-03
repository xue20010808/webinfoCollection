from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)
domamin=input('input the domain u wanna check the CDN info:\n')
driver.get(f'http://ping.chinaz.com/{domamin}')
time.sleep(0.5)
print('conduct the whole Chinaping....')
time.sleep(0.5)
print('please wait',end='')
time.sleep(0.5)
print('..',end='')
time.sleep(0.5)
print('..',end='')
time.sleep(0.5)
print('..',)
time.sleep(5)
print('The CDN info:')
#//*[@id="ipliststr"]/a[1]   //*[@id="ipliststr"]/a[2]
iplist=[]
for i in range(1,9):
   try:
     el=driver.find_element_by_xpath(f'//*[@id="ipliststr"]/a[{i}]')
     iplist.append(el.text)
   except:
       break
if len(iplist) >1:
    print('\033[1;31m【*】CDN exist\033[0m')
    for i in iplist:
        print(i)
    print(f'more info please check in http://ping.chinaz.com/{domamin}')
else:
    print(' NO CDN BEing used .... ')
    print(f'the  true ipaddress is {iplist[0]}')