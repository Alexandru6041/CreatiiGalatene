import binascii
import email
from struct import Struct
from urllib.error import HTTPError
from cryptography.fernet import Fernet
import os
import sys

from cv2 import estimateTranslation3D
sys.path.append(os.path.dirname(__file__))
import random
import base64
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
from cryptography.fernet import Fernet
import urllib3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.base import MIMEBase
from pathlib import Path
import random
from math import sqrt, ceil, floor
salt = "663ba00c232b3663ba00c232b3e42"
current_dir = os.getcwd()
pins = []
user_data = []
emails = []
errors_email = "errors.creatiigalatene@gmail.com"
password = "MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAl50wqLncIdlcavZiegZ3"
from math import ceil, floor, sqrt
key = b'DpB6D2AxmzeQHETiBWKVWoqFXY0hS3ClhG51dxgWtSE='
fernet = Fernet(key)
def encryption(string):
    string = str(string)
    encMes = fernet.encrypt(string.encode())
    return str(encMes)
            
def decription(string):
    string = str(string)[1:]
    string = string.encode()
    decMes = fernet.decrypt(string).decode()
    return decMes
def hash_string(string):
    string = str(string).encode("utf-8")
    return str(hashlib.sha512(string).hexdigest())[:100]
def compare_strings(string1, string2):
    if string1 == string2:
        return True
    else:
        return False
def email_me_error(error):
    sender_mail = "help.creatiigalatene@gmail.com"
    password = 'casnpyzwzfakimdr'
    message = MIMEMultipart("alternative")
    message["Subject"] = "Eroare!"
    message["From"] = sender_mail
    message["To"] = errors_email
    text = error
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_mail, password="casnpyzwzfakimdrv")
        server.sendmail(sender_mail, errors_email, message.as_string())
def email_me(Subject, Context, user_email):
    i = 0
    while i < 1:
        sender_mail = "help.creatiigalatene@gmail.com"
        password = 'casnpyzwzfakimdr'
        message = MIMEMultipart("alternative")
        message["Subject"] = Subject
        message["From"] = sender_mail
        message["To"] = user_email
        text = Context
        part1 = MIMEText(text, "plain")
        message.attach(part1)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_mail, password="casnpyzwzfakimdr")
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

@app.route('/Acasa', methods=["GET", "POST"])
def Acasa():
    email_user = None
    username = None
    logged_in = False
    data_articles = ''
    username_encrypted = None
    username_encrypt = ''
    password_encrypted = None
    password_encrypt = ''
    i = 1
    try:
        sqliteConnection = sqlite3.connect('main.db')
        cursor = sqliteConnection.cursor()
    except sqlite3.Error as e:
        email_me_error(e)
    page_url = request.url
    cursor.execute("SELECT * FROM Articles")
    sqliteConnection.commit()
    data_articles = cursor.fetchall()
    if("?" in str(page_url)):
        email_input = request.args["email"]
        password_input = request.args["password"]
        email_input = decription(email_input)
        password_input = decription(password_input)
        cursor.execute("SELECT * FROM UserData WHERE Email = ? OR Username = ?", [email_input, email_input])
        sqliteConnection.commit()
        data = cursor.fetchall()
        for row in data:
            if(row[2] == password_input):
                logged_in = True
                username = row[0]
                password = row[2]
                username_encrypt = encryption(str(username))
                password_encrypt = encryption(str(password))
    return render_template("index.html", username=username, logged_in=logged_in, username_encrypted=username_encrypt, password_encrypted=password_encrypt, articles = data_articles, i = i)

@app.route("/Profile", methods=["POST", "GET"])
def Profile(): 
    profile_url = request.url
    if("?" in str(profile_url)):
        username = request.args["username"]
        password = request.args["password"]
        username_encrypted = username
        password_encrypted = password
        try:
            sqliteConnection = sqlite3.connect('main.db')
            cursor = sqliteConnection.cursor()
        except sqlite3.Error as e:
            email_me_error(e)
        username = decription(username)
        cursor.execute("SELECT * FROM UserData WHERE username = ?", [username])
        sqliteConnection.commit()
        data = cursor.fetchall()
        for row in data:
            if(row[2] == password):
                pass
    return render_template("profile.html", username_encrypt = username_encrypted, password_encrypt = password_encrypted)
@app.route("/ArticoleleMele", methods = ["POST", "GET"])
def MyArticles():
    url = request.url
    article_bool = False
    count = 0
    try:
        sqliteConnection = sqlite3.connect('main.db')
        cursor = sqliteConnection.cursor()
    except sqlite3.Error as e:
        email_me_error(e)
    if("?" in str(url)):
        username = request.args["username"]
        password = request.args["password"]
        
        username_encrypted = username
        password_encrypted = password
        username = decription(username)
        data_number = cursor.execute("SELECT * FROM Articles WHERE Author = ?", [username])
        sqliteConnection.commit()
        data_number = cursor.fetchall()
        print(len(data_number))
        if(len(data_number) > 0):
            article_bool = True
        data_main = cursor.execute("SELECT * FROM Articles WHERE Author = ?", [username])
        sqliteConnection.commit()
        data = cursor.fetchall()
        
    return render_template("MyArticles.html", article_bool = article_bool, values = data, username = username_encrypted, password = password_encrypted, article_no = len(data_number))


@app.route("/MyArticles_Detail", methods = ["POST", "GET"])
def article():
    url = request.url
    try:
        sqliteConnection = sqlite3.connect("main.db")
        cursor = sqliteConnection.cursor()
    except sqlite3.error as e:
        email_me_error(e)
    if("?" in str(url)):
        Id_user = request.args["id"]
        username = request.args["username"]
        password = request.args["password"]
        username_decrypted = decription(username)
        password_decrypted = decription(password)
        cursor.execute("SELECT * FROM UserData WHERE Username=?", [username_decrypted])
        sqliteConnection.commit()
        data = cursor.fetchall()
        for row in data:
            if(password_decrypted == row[2]):      
                cursor.execute("SELECT * FROM Articles WHERE Id=?", [Id_user])
                sqliteConnection.commit()
                data2 = cursor.fetchall()
    return render_template("MyArticles_Detail.html", values=data2)
@app.route("/AdaugareArticol", methods=["POST", "GET"])
def adaugare_articol():
    error = None
    url = request.url
    try:
        sqliteConnection = sqlite3.connect('main.db')
        cursor = sqliteConnection.cursor()
    except sqlite3.Error as e:
        email_me_error(e)
    if("?" in str(url)):
        username = request.args["username"]
        password = request.args["password"]
        username_encrypted = username
        password_encrypted = password
        username = decription(username)
        if request.method == "POST":
            Title = request.form["title"]
            Article_Text = request.form["context_article"]
            Article_Description = request.form["description_article"]
            if(len(Article_Description) > 300):
                error = "Descrierea este prea lunga"
            cursor.execute("SELECT * FROM UserData WHERE username = ?", [username])
            sqliteConnection.commit()
            data = cursor.fetchall()
            for row in data:
                username = decription(username_encrypted)
                user_password = row[2]
                user_email = row[1]
                user_function = row[3]
                user_id = row[4]
                article_id = make_pin(8)
                commit_likes = 0
                if(error == None):
                    cursor.execute("INSERT INTO Articles VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [username, Title, Article_Description, Article_Text, user_function, user_email, article_id, commit_likes])
                    sqliteConnection.commit()
                    email_me("Felicitari pentru postarea unui nou articol: " + Title , "Articolul dumneavoastra intitulat ' " + Title + " ' a fost urcat cu succes pe platforma CreatiiGalatene", user_email)
    return render_template("adauga_articol.html", username=username_encrypted, password=password_encrypted, error = error)
@app.route("/ArticleRead", methods=["GET", "POST"])
def ARead():
    url = request.url
    error = None
    liked_article_by_user = False
    data = []
    logged_in = True
    ok = 1
    try:
        sqliteConnection = sqlite3.connect('main.db')
        cursor = sqliteConnection.cursor()
    except sqlite3.Error as e:
        email_me_error(e)
    if("?" in str(url)):
        id_article = request.args["id"]
        username = request.args["username"]
        if(username == "NULL"):
            logged_in = False
        cursor.execute("SELECT * FROM Liked WHERE Id = ?", [id_article])
        sqliteConnection.commit()
        data = cursor.fetchall()
        for row in data:
            if(logged_in == True):
                if(str(decription(username)) == row[1]):
                    liked_article_by_user = True
        if(liked_article_by_user == False and ok == 1):
            if(request.method == "POST"):
                if(logged_in == False):
                    error = "Trebuie sa fiti autentificat ca sa apreciati articolul"
                    cursor.execute(
                        "SELECT * FROM Articles WHERE Id = ?", [id_article])
                    sqliteConnection.commit()
                    data = cursor.fetchall()
                    return render_template("ARead.html", error=error, data=data, liked_article_by_user=liked_article_by_user, Id=id_article, username=username)

                cursor.execute("SELECT * FROM Articles WHERE Id = ?", [id_article])
                sqliteConnection.commit()
                data = cursor.fetchall()
                for row in data:
                    likes = row[7]
                    likes = int(likes) + 1
                    cursor.execute("UPDATE Articles SET Likes = ? WHERE Id = ?", [likes, id_article])
                    sqliteConnection.commit()
                    cursor.execute("INSERT INTO Liked VALUES (?, ?)", [id_article, decription(username)])
                    sqliteConnection.commit()
                    print("OK Liked", likes)
                    cursor.execute(
                        "SELECT * FROM Articles WHERE Id = ?", [id_article])
                    sqliteConnection.commit()
                    data = cursor.fetchall()
                liked_article_by_user = True
                ok = 0
        if(liked_article_by_user == True and ok == 1):
            if(request.method == "POST"):
                cursor.execute(
                    "SELECT * FROM Articles WHERE Id = ?", [id_article])
                sqliteConnection.commit()
                data = cursor.fetchall()
                for row in data:
                    likes = row[7]
                    likes = int(likes) - 1
                    cursor.execute("UPDATE Articles SET Likes = ? WHERE Id = ?", [
                                likes, id_article])
                    sqliteConnection.commit()
                    cursor.execute("DELETE FROM Liked WHERE Id = ? AND Username = ?", [id_article, decription(username)])
                    sqliteConnection.commit()
                    print("OK Unliked", likes)
                    cursor.execute(
                        "SELECT * FROM Articles WHERE Id = ?", [id_article])
                    sqliteConnection.commit()
                    data = cursor.fetchall()
                liked_article_by_user = False
                ok = 0
        cursor.execute("SELECT * FROM Articles WHERE Id = ?", [id_article])
        sqliteConnection.commit()
        data = cursor.fetchall()
    return render_template("ARead.html", error = error, data = data, liked_article_by_user = liked_article_by_user, Id = id_article, username = username)
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
        if(len(email_input) > 100):
            error = "Emailul este prea lung"
            return render_template("sign-up.html", error=error)
        cursor.execute("SELECT * FROM UserData WHERE Email=?", [email_input])
        sqliteConnection.commit()
        data = cursor.fetchall()
        for row in data:
            if (row[1] == email_input):
                error = "Deja exista un cont cu aceasta adresa de email"
                return render_template("sign-up.html", error=error)

        username_input = request.form["username_field"]
        if(len(username_input) > 50):
            error = "Numele este prea lung"
            return render_template("sign-up.html", error=error)
        cursor.execute("SELECT * FROM UserData WHERE Username=?", [username_input])
        sqliteConnection.commit()
        data = cursor.fetchall()
        for row in data:
            if (row[0] == username_input):    
                error = "Numele de utilizator este deja luat"    
                return render_template("sign-up.html", error=error)

        ocupation_input = request.form["User_Ocupation"]
        if(len(ocupation_input) > 100):
            error = "Numele ocupatiei este prea lung"
            return render_template("sign-up.html", error=error)
        password_input = request.form["password_field"]
        if(len(password_input) > 255):
            error = "Parola este prea lunga"
            return render_template("sign-up.html", error=error)
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
            email_me("Codul de confirmare: ", account_id, email_input)
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
        cursor.execute("SELECT * FROM UserData WHERE Email = ? OR Username = ?", [email_input, email_input])
        sqliteConnection.commit()
        data = cursor.fetchall()
        password_input = hash_string(str(password_input))
        for row in data:
            if(row[2] == password_input):
                encrypted_email = encryption(str(email_input))
                encrypted_password = encryption(str(password_input))
                return redirect("/Acasa?email=" + str(encrypted_email) + "&password=" + str(encrypted_password))
            
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
                email_me("Schimbare parola: ", generated_code, email_input)
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
    app.run(host = '0.0.0.0')