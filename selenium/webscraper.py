from selenium import webdriver
#from time import sleep

chrome_path = "/Users/jesusmedina/Downloads/chromedriver"
chrome = webdriver.Chrome(chrome_path)

chrome.get("https://www.adidas.com/us/men-running-shoes")
#shoes = chrome.find_elements_by_class_name("gl-price")[0]
shoes = chrome.find_elements_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[11]/div/div/div/div[2]/a/div[2]/div[2]')[0]
shoes_text = shoes.text

for i in shoes_text:
    print(i)

input("Enter anything to quit")
chrome.close()
print("finished")