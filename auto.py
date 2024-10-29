from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option=webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=option)

driver.get("https://ap6.fscloud.com.cn/t/laifen")

time.sleep(3)
driver.maximize_window()

driver.find_element(By.ID, 'username').send_keys('huangqian')
driver.find_element(By.ID, 'password').send_keys('Laifen@2022')
driver.find_element(By.ID, 'kc-login').click()
driver.find_element(By.XPATH,'//*[@id="global-app"]/div/div/div[1]/div/div/div[2]/ul/li[3]/div').click()

time.sleep(5)

driver.quit()