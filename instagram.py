from instapy_cli import client
from information import username, password
import random
import time


image = '/Users/jesusmedina/Python/IMG_7690.jpeg'
caption = 'The day I married the love of my life @stephaniet12714. #doneonpython'

with client(username, password) as cli:
    cli.upload(image, caption)

print('Post have been uploaded')