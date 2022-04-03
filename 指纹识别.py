from selenium import webdriver
from selenium.webdriver.common.by import By
import time
domain=input('input domain:\n')
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)
driver.get('http://whatweb.bugscaner.com/look/')
el=driver.find_element_by_xpath('//*[@id="inputurls"]')
el.clear()
time.sleep(2)
el.send_keys(f'{domain}')
cel=driver.find_element_by_xpath('//*[@id="start"]')
cel.click()
print('please wait',end='')
time.sleep(0.5)
print('..',end='')
time.sleep(0.5)
print('..',end='')
time.sleep(0.5)
print('..',)
time.sleep(5)
#//*[@id="cms"]/div[1]  //*[@id="cms"]/div[2]
for i in range(1,15):
    try:
        el1=driver.find_element_by_xpath(f'//*[@id="cms"]/div[{i}]')
        print(el1.text)
    except:
        print('info doesnt exist')
print('more info in http://whatweb.bugscaner.com/look/')