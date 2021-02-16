from selenium import webdriver


driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://web.whatsapp.com/')
input('Scan the QR code then press Enter')
msg = input('Enter your massage :')
num = int(input('How many massage :'))
name = input('Contact(s) :')
name.split(',')
title = "//span[@title='{}']".format(name)

user = driver.find_element_by_xpath(title)
user.click()
msg2 = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for a in range(num):
    msg2.send_keys(msg)
    cl = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
    cl.click()