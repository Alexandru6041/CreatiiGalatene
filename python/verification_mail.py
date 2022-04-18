import os
try:
    import hashlib
except ImportError:
    os.system("pip3 install hashlib")
from datetime import datetime as dt
from time import sleep
try:
    import ssl
except ImportError:
    os.system("pip3 install ssl")
try:
    import urllib3
except ImportError:
    os.system("pip3 install urllib3")
try:
    from email.mime.text import MIMEText
except ImportError:
    os.system('python -m pip install email')
try:
    from email.mime.multipart import MIMEMultipart
except ImportError:
    os.system('python -m pip install email')
try:
    from email.mime.base import MIMEBase
except ImportError:
    os.system('python -m pip install email')
try:
    import django
except ImportError:
    os.system("python -m pip3 install django")
try:
    import flask
except ImportError:
    os.system('python -m pip3 install flask')
salt = "663ba00c232b3663ba00c232b3e42"
working_folder = os.getcwd()
##IN WORKING NEED TO DO DATABSE AND FORM