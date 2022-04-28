import os
import sys
sys.path.append(os.path.dirname(__file__))

import random
from ast import Import
from ssl import AlertDescription
from flask import *
import re
import sqlite3
import cgi
from pathlib import Path
from time import sleep
import hashlib
from time import sleep
import ssl
import urllib3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.base import MIMEBase
from pathlib import Path
import random
salt = "663ba00c232b3663ba00c232b3e42"
current_dir = os.getcwd()
pins = []
user_data = []
emails = []
errors_email = "errors.creatiigalatene@gmail.com"
def hash_string(string):
    string = str(string).encode('utf-8')
    return hashlib.sha512(string).hexdigest()

def compare_strings(string1, string2):
    if string1 == string2:
        return True
    else:
        return False
def email_me_error(error):
    sender_mail = "help.creatiigalatene@gmail.com"
    password = 'vomgip-mAfzih-7hafty'
    message = MIMEMultipart("alternative")
    message["Subject"] = "Eroare!"
    message["From"] = sender_mail
    message["To"] = errors_email
    text = error
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_mail, password="vomgip-mAfzih-7hafty")
        server.sendmail(sender_mail, errors_email, message.as_string())
def email_me(generated_code, user_email):
    i = 0
    while i < 1:
        sender_mail = "help.creatiigalatene@gmail.com"
        password = 'vomgip-mAfzih-7hafty'
        message = MIMEMultipart("alternative")
        message["Subject"] = ""
        message["From"] = sender_mail
        message["To"] = user_email
        text = str(generated_code)
        part1 = MIMEText(text, "plain")
        message.attach(part1)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_mail, password="vomgip-mAfzih-7hafty")
            server.sendmail(sender_mail, user_email, message.as_string())
        i += 1
    if(i == 1):
        return 0
# con_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + str(current_dir) + "/MainDB.accdb"
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
def make_pin(length):
    combined_list = digits
    string = ''
    decrypt_password = string.join(random.sample(combined_list, length))
    return decrypt_password

app = Flask(__name__)
@app.route('/')

@app.route('/Acasa')
def Acasa():
    return render_template("index.html")

@app.route("/SignUp", methods = ["POST", "GET"])
def SignUp():
    error = None
    try:
        sqliteConnection = sqlite3.connect('main.db')
        cursor = sqliteConnection.cursor()
    except sqlite3.Error as e:
        email_me_error(e)
        error = "Nu s-a putut realiza conexiunea la baza de date"
        print("Error in database: " + e)
    if request.method == "POST":
        email_input = request.form["email_field"]
        cursor.execute("SELECT * FROM UserData WHERE Email=?", [email_input])
        sqliteConnection.commit()
        data = cursor.fetchall()
        for row in data:
            if (row[1] == email_input):
                error = "Deja exista un cont cu aceasta adresa de email"
                return render_template("sign-up.html", error=error)

        username_input = request.form["username_field"]
        cursor.execute("SELECT * FROM UserData WHERE Username=?", [username_input])
        sqliteConnection.commit()
        data = cursor.fetchall()
        for row in data:
            if (row[0] == username_input):    
                error = "Numele de utilizator este deja luat"    
                return render_template("sign-up.html", error=error)

        ocupation_input = request.form["User_Ocupation"]
        password_input = request.form["password_field"]
        conf_password_input = request.form["confirm_password_field"]
        if(password_input != conf_password_input):
            error = "Parolele nu coincid"
        else:
            account_id = make_pin(8)
            hash_string(str(password_input))
            user_data.append(username_input) 
            user_data.append(email_input) 
            user_data.append(password_input)
            user_data.append(ocupation_input)
            user_data.append(account_id)
            email_me(account_id, email_input)
            pins.append(account_id)
            return redirect("/ConfirmareEmail")
    return render_template("sign-up.html", error = error)

@app.route("/ConfirmareEmail", methods=["GET", "POST"])
def confirm_email():
    error = None
    try:
        sqliteConnection = sqlite3.connect('main.db')
        cursor = sqliteConnection.cursor()
    except sqlite3.Error as e:
        email_me_error(e)
        error = "Nu s-a putut realiza conexiunea la baza de date"
        return render_template("confirm_email_account_create.html", error = error)
    generated_code = pins[-1]
    if request.method == "POST":
        input_code = request.form["user_input_code"]
        input_code = str(input_code)
        user_data[2] = hash_string(str(user_data[2]))
        if input_code == generated_code:
            cursor.execute("INSERT INTO UserData VALUES (?, ?, ?, ?, ?)", [user_data[0], user_data[1], user_data[2], user_data[3], user_data[4]])
            sqliteConnection.commit()
            return redirect("/Acasa")
        else:
            error = "Cod de confirmare incorect"
    return render_template("confirm_email_account_create.html", error = error)

@app.route("/LogIn", methods=["POST","GET"])
def LogIn():
    error = None
    if request.method == "POST":
        email_input = request.form["email_field"]
        password_input = request.form["password_field"]
        try:
            sqliteConnection = sqlite3.connect('main.db')
            cursor = sqliteConnection.cursor()
        except sqlite3.Error as e:
            email_me_error(e)
            error = "Nu a fost posibila conexiunea la baza de date"
        cursor.execute("SELECT * FROM UserData WHERE Email = ?", [email_input])
        sqliteConnection.commit()
        data = cursor.fetchall()
        password_input = hash_string(str(password_input))
        for row in data:
            if(row[2] == password_input):
                return redirect("/Acasa")
        error = "Credentiale Incorecte!"    
        return render_template("log-in.html", error = error)
    return render_template("log-in.html", error=error)

@app.route("/passwordTrue", methods=["GET", "POST"])
def password_true():
    error = None
    grate = None
    if request.method == "POST":
        try:
            sqliteConnection = sqlite3.connect('main.db')
            cursor = sqliteConnection.cursor()
        except sqlite3.Error as e:
            email_me_error(e)
            error = "Nu a fost posibila conexiunea la baza de date"
        new_pass = request.form["parola1"]
        new_pass_confirm = request.form["parola2"]
        email_input = emails[-1]
        if(new_pass == new_pass_confirm):
            new_pass = hash_string(str(new_pass))
            cursor.execute("UPDATE UserData SET User_Password = ? WHERE Email = ?", [new_pass, email_input])
            sqliteConnection.commit()
            grate = "Parola a fost schimbata cu succes!"
            return render_template("change_pass_trueverify.html", grate = grate)
        else:
            error = "Parolele nu coincid"
    return render_template("change_pass_trueverify.html", error = error)
@app.route("/AdresaEmailPass", methods=["GET", "POST"])
def AdresaEmailPass():
    error = None
    if request.method == "POST":
        email_input = request.form["email_input"]
        generated_code = make_pin(length=8)
        try:
            sqliteConnection = sqlite3.connect('main.db')
            cursor = sqliteConnection.cursor()
        except sqlite3.Error as e:
            email_me_error(e)
            error = "Nu a fost posibila conexiunea la baza de date"
        cursor.execute("SELECT * FROM UserData WHERE Email = ?", [email_input])
        sqliteConnection.commit()
        data = cursor.fetchall()
        for row in data:
            if row[1] == email_input:
                email_me(generated_code, email_input)
                pins.append(generated_code)
                emails.append(email_input)
                return redirect("/SchimbareParola")
        error = "Nu exista cont cu aceasta adresa de email"
    return render_template("get_email_only.html", error = error)
    
@app.route("/SchimbareParola", methods = ["POST", "GET"])
def ConfirmareCod():
    error = None
    generated_code = pins[-1]
    
    if request.method == "POST":
        input_code = request.form["user_input_code"]
        input_code = str(input_code)
        if input_code == generated_code:
            return redirect("/passwordTrue")
        else:
            error = "Codul de confirmare a fost introdus gresit"

    return render_template("change_pass_email_confirm.html", error = error)

if __name__ == "__main__":
    app.run(debug = True, port = 5500)