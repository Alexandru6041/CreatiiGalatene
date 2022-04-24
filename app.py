import random
from ast import Import
import os
from ssl import AlertDescription
from flask import Flask, render_template, request, redirect, url_for, session
import re
import pyodbc
import cgi
from pathlib import Path
from time import sleep
import hashlib
from time import sleep
import ssl
import urllib3
from random import randint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.base import MIMEBase
salt = "663ba00c232b3663ba00c232b3e42"
current_dir = os.getcwd()
def encrypt_string(string):
    string = str(string).encode('utf-8')
    return hashlib.sha512(string).hexdigest()

def compare_strings(string1, string2):
    return string1 is string2

def email_me(username, generated_code, user_email):
    sender_mail = "help.creatiigalatene@gmail.com"
    password = 'vomgip-mAfzih-7hafty'
    message = MIMEMultipart("alternative")
    message["Subject"] = str(username) + ": Schimbare Parola CreatiiGalatene"
    message["From"] = sender_mail
    message["To"] = user_email
    text = "Salut, acest email contine codul de confirmare pentru schimbarea parolei tale de creator desavarsit.\n\n\n" + \
        str(generated_code)
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_mail, password="vomgip-mAfzih-7hafty")
        server.sendmail(sender_mail, user_email, message.as_string())
# con_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + str(current_dir) + "/MainDB.accdb;"
# conn = pyodbc.connect(con_string)
# cursor = conn.cursor()
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
locase_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z']
upcase_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
               'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '*',
           '(', ')', '-', '_', ',', '<', '.', '>', '/', '?', '"', ':', ';']
app = Flask(__name__)
@app.route('/')

@app.route('/Acasa')
def Acasa():
    return render_template("index.html")

@app.route("/SignUp", methods = ["POST", "GET"])
def SignUp():
    if request.method == "POST":
        email_input = request.form["email_field"]
        username_input = request.form["username_field"]
        password_input = request.form["password_field"]
        conf_password_input = request.form["confirm_password_field"]
        if(password_input != conf_password_input):
            return render_template("sign-up.html")
    return render_template("sign-up.html")

@app.route("/LogIn", methods=["POST","GET"])
def LogIn():
    if request.method == "POST":
        email_input = request.form["email_field"]
        password_input = request.form["password_field"]
        # User_Data = cursor.execute("SELECT * FROM UserData WHERE mail = ?", email_input)
        # conn.commit()
        #SQL Command wrong, read the documentation
        #HUGE ISSUE
        #NO SIBIU BACKEND
        #data = cursor.fetchall()
        for row in data:
            if email_input == row[1]:
                print("mail: " + email_input)
            else:
                sleep(2)
                return render_template("sign-up.html")
    return render_template("log-in.html")

@app.route("/SchimbareParola", methods = ["POST", "GET"])
def ConfirmareCod():
    def make_pin(length):
        combined_list = digits + upcase_char + locase_char + symbols
        string = ''
        decrypt_password = string.join(random.sample(combined_list, length))
        return decrypt_password
    user_email = 'alexchelariu834@gmail.com'
    username = 'Alexandru6041'
    generated_code = make_pin(randint(13, 20))
    generated_code = str(generated_code).encode('utf-8')
    generated_code_hash = encrypt_string(str(generated_code))
        
    email_me(username, generated_code, user_email)
    if request.method == "POST":
        input_code = request.form["user_input_code"]
        hash_input_code = encrypt_string(input_code)
        if compare_strings(hash_input_code, generated_code_hash) == 1:
            return render_template("change_pass_trueverify.html")
        else:
            return render_template("log-in.html")
        
    return render_template("change_pass_email_confirm.html")   

@app.route("/passwordTrue")
def password_true():
     return render_template("change_pass_trueverify.html")
 
if __name__ == "__main__":
    app.run(debug = True, port = 5500)