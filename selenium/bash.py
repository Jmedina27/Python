import getpass
import os
import wget
import zipfile

username = getpass.getuser()
str(username)

name = 'Users/%s/Documents/Marshall' % username

os.system('mkdir /Users/%s/Documents/Marshall' % username)
url = 'https://chromedriver.storage.googleapis.com/78.0.3904.11/chromedriver_mac64.zip'
wget.download(url, '/Users/jesusmedina/Documents/Marshall/chromedriver')

with zipfile.ZipFile('/Users/jesusmedina/Documents/', 'r') as zip_ref:
    zip_ref.extract('chromedriver')