from selenium import webdriver
from time import sleep

user = input("Enter the email: ")
password = "donthackme27"
url = "https://www.facebook.com"

driver = webdriver.Chrome('/Users/jesusmedina/Downloads/chromedriver')
driver.get(url)

print("opened facebook")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(user)
print("username entered")
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(password)
print("password entered")
sleep(2)

login = driver.find_element_by_id("loginbutton")
login.click()

print("done")
input("Enter anything to quit")
driver.quit()
print("finished")