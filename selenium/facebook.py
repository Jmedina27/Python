from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

user = input("Enter the email: ")
password = input("enter the password : ")
url = "https://www.facebook.com"

driver = webdriver.Chrome('/Users/jesusmedina/Downloads/chromedriver')
driver.get(url)

print("opened facebook")

username_box = driver.find_element_by_id('email')
username_box.send_keys(user)
print("username entered")

password_box = driver.find_element_by_id('pass')
password_box.send_keys(password)
print("password entered")

login = driver.find_element_by_id("loginbutton")
login.click()

print("done")

sleep(5)

logout = driver.find_element_by_id("logoutMenu")
logout.click()

#driver.find_element_by_xpath('//*[@id="js_5e"]/div/div/ul/li[12]/a').click()
post = driver.find_element(By.XPATH,'//*[@id="js_8f"]/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div')
sleep(2)
post.send_keys("Hello, World!")
#input("Enter anything to quit")
#driver.quit()
#print("finished")
