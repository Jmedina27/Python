from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import xlwt
from xlwt import Workbook
from openpyxl import load_workbook
import getpass



ren_user = input('Enter username: ')
ren_passwd = input('Enter password: ')

name = getpass.getuser()

url = "https://hosted13.renlearn.com/272178/public/rpm/login/Login.aspx?srcID=t"

# option for headless selenium chrome driver
options = Options()
chrome_path = '/Users/%s/Downloads/chromedriver' % str(name)
options.headless = True
chrome = webdriver.Chrome(executable_path=chrome_path, options=options)

# launching chrome with the desired url in the background
chrome.get(url)

# logging into account
username = chrome.find_element_by_id('tbUserName')
username.send_keys(ren_user)

password = chrome.find_element_by_id('tbPassword')
password.send_keys(ren_passwd)

login = chrome.find_element_by_id('btnLogIn')
login.click()
sleep(1)

account_name = chrome.find_element_by_id('ctl00_mHeader_aUsername').text
print('Logged in as ' + account_name)

# switching to student users page
usrs = chrome.find_element_by_id('app-users')
usrs.click()
sleep(1)

view = chrome.find_element_by_id('m_lnkViewStudent')
view.click()
sleep(1)
print('Going to Student Users')

# creating lists for student name, student username, and password
name_list = []
username_list = []
pass_list = []

wb = Workbook()

def get_students(teacher_option, teacher_name):
    # choosing teacher options to view
    select = chrome.find_element_by_xpath(teacher_option)
    select.click()
    send = chrome.find_element_by_id('btnSearch')
    send.click()
    # switching to see student login information
    paswrds = chrome.find_element_by_id('ctl00_cp_Content_tabPasswords')
    paswrds.click()
    sheet1 = wb.add_sheet(teacher_name)
    sheet1.write(0, 0, 'Student Name')
    sheet1.write(0, 1, 'Username')
    sheet1.write(0, 2, 'Password')

    # creating lists for student name, student username, and password
    name_list = []
    username_list = []
    pass_list = []

    i = 0
    x = 1
    while i < 36:

        if x < 10:
            name_id = 'ctl00_cp_Content_rptPW_ctl0' + str(x) + '_tdStudent'
            username_id = 'ctl00_cp_Content_rptPW_ctl0' + str(x) + '_tdUserName'
            pass_id = 'ctl00_cp_Content_rptPW_ctl0' + str(x) + '_tdPW'
            student_name = chrome.find_elements_by_id(name_id)
            student_username = chrome.find_elements_by_id(username_id)
            student_passwd = chrome.find_elements_by_id(pass_id)

            for j in student_name:
                name_list.append(j.text)
            for j in student_username:
                username_list.append(j.text)
            for j in student_passwd:
                pass_list.append(int(j.text))

            x += 1
        else:
            name_id = 'ctl00_cp_Content_rptPW_ctl' + str(x) + '_tdStudent'
            username_id = 'ctl00_cp_Content_rptPW_ctl' + str(x) + '_tdUserName'
            pass_id = 'ctl00_cp_Content_rptPW_ctl' + str(x) + '_tdPW'
            student_name = chrome.find_elements_by_id(name_id)
            student_username = chrome.find_elements_by_id(username_id)
            student_passwd = chrome.find_elements_by_id(pass_id)

            for j in student_name:
                name_list.append(j.text)
            for j in student_username:
                username_list.append(j.text)
            for j in student_passwd:
                pass_list.append(int(j.text))
            x += 1

        i += 1

    x = 1
    for j in name_list:
        sheet1.write(x, 0, j)
        x += 1
    x = 1
    for j in username_list:
        sheet1.write(x, 1, j)
        x += 1
    x = 1
    for j in pass_list:
        sheet1.write(x, 2, j)
        x += 1
    print(teacher_name + '-> DONE')

    name = getpass.getuser()

    wb.save('/Users/%s/Desktop/STAR.xls' % name)

teachers = []
teachers_name = ['Amori', 'Bruyneel', 'Cortez', 'DeAnda', 'Delhauer', 'Griffin', 'Herrera', 
'King', 'Johnson', 'Melcher', 'Mercado', 'Mestlin', 'Miller', 'Morris', 'Noriega', 'Ramos', 'Rodarte', 'Zataray']

x = 6
for i in range(len(teachers_name)):
    teachers.append('//*[@id="ctl00_cp_Content_ddlClasses"]/option[' + str(x) + ']')
    x += 1

for i, j in zip(teachers, teachers_name):
    get_students(teacher_option=i, teacher_name=j)


print('Finished')
