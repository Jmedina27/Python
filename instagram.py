from instapy_cli import client
import random
import time

username = input('Enter username: ')
password = input('Enter password: ')

image = 'path_to_img'
caption = input('Enter a caption: ')

with client(username, password) as cli:
    cli.upload(image, caption)

print('Post have been uploaded')