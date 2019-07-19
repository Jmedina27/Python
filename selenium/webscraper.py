from selenium import webdriver
from time import sleep
chrome_path = "/Users/jesusmedina/Downloads/chromedriver"
chrome = webdriver.Chrome(chrome_path)

chrome.get("https://www.adidas.com/us/men-running-shoes")
shoes = chrome.find_elements_by_class_name("gl-product-card__name gl-label gl-label--m")

for i in shoes:
    print(i)

#input("Enter anything to quit")
#chrome.close()
#print("finished")