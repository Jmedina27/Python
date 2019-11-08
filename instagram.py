from instapy_cli import client
import random
import time
import getpass

username = input('Enter username: ')
password = getpass.getpass('Enter password: ')

image = '/User/Downloads/KTC_new_logo.png'
caption = input('Enter a caption: ')

with client(username, password) as cli:
    cli.upload(image, caption)

client()._login()
print('Post has been uploaded')