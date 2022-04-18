from ast import Import


import os
os.system("pip3 install configparser")
try:
    from flask import Flask, render_template, request, redirect, url_for, session
except ImportError:
    os.system("pip3 install flask")
try:
    from flask_mysqldb import MySQL
except ImportError:
    os.system("pip install Flask-MySQLdb")
try:
    import MySQLdb.cursors
except ImportError:
    os.system('pip3 install MySQL-python')    
try:
    import re
except ImportError:
    os.system('pip3 install regex')
app = Flask(__name__)
app.secret_key = "mWJA&&-84%tyWKuVKzpdke7P3dmLEVB#A%w!aqx7f7A6wWvmUS"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mWJA&&-84%tyWKuVKzpdke7P3dmLEVB#A%w!aqx7f7A6wWvmUS'
app.config['MYSQL_DB'] = 'creatiigalatene'
mysql = MySQL(app)
