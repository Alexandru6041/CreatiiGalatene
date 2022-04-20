from ast import Import
import os
from flask import Flask, render_template, request, redirect, url_for, session
import re
import pyodbc
import cgi
from pathlib import Path

app = Flask(__name__)
@app.route('/')

@app.route('/Acasa')
def Acasa():
    return render_template("index.html")

@app.route("/SignUp")
def SignUp():
    return render_template("sign-up.html")

@app.route("/LogIn", methods=["POST","GET"])
def LogIn():
    if request.method == "POST":
        email_input = request.form["email_field"]
        password_input = request.form["password_field"]
        current_dir = os.getcwd()
        con_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + str(current_dir) + "/MainDB.accdb;"
        conn = pyodbc.connect(con_string)
        cursor = conn.cursor()
        User_Data = cursor.execute("SELECT * FROM UserData")
        data = cursor.fetchall()
        print("Email: " + email_input + "\nPassword: " + password_input)
    return render_template("log-in.html")
if __name__ == "__main__":
    app.run(debug = False, host = '0.0.0.0')