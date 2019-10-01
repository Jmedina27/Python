from selenium import webdriver
from time import sleep
import xlwt
from xlwt import Workbook

#create chrome object that uses Chrome Browser 
chrome = webdriver.Chrome("/Users/jesusmedina/Downloads/chromedriver")

#go to the link using the chrome browser
chrome.get("https://www.sephora.com/beauty/new-makeup?icid2=meganav_new_justarrived_makeup_link")

#create two obv
name = chrome.find_elements_by_class_name("css-ktoumz")
price = chrome.find_elements_by_class_name("css-68u28a")

name_list = []
price_list = []

for i in name:
    name_list.append(i.text)
for i in price:
    price_list.append(i.text)

mapped = [name_list, price_list]

for i in zip(*mapped):
   print(*i)

wb = Workbook()

sheet1 = wb.add_sheet("sephora")
sheet1.write(0, 0, 'Product Name')
sheet1.write(0, 1, 'Product Price')

x = 1
for i in name_list:
    sheet1.write(x, 0, i)
    x += 1

x = 1
for i in price_list:
    sheet1.write(x, 1, i)
    x += 1

wb.save('sephora.xls')

input("hit enter to quit the program")
chrome.close()
print("Finished")