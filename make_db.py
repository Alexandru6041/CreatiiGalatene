import sqlite3
try:
    sqliteConnection = sqlite3.connect('main.db')
    cursor = sqliteConnection.cursor()
except sqlite3.Error as e:
    print("Error in database: " + e)
User_data_table = """
    CREATE TABLE UserData(
        Username VARCHAR(50) NOT NULL,
        Email VARCHAR(255) NOT NULL,
        User_Password VARCHAR(255) NOT NULL,
        Function VARCHAR(255) NOT NULL,
        Id INT
    );
"""
cursor.execute(User_data_table)
Articles_table = """
    CREATE TABLE Articles(
        Author VARCHAR(255) NOT NULL,
        Title VARCHAR(255) NOT NULL,
        Description VARCHAR(255) NOT NULL, 
        Context VARCHAR(3000) NOT NULL,
        Id INT
    );
"""
cursor.execute(Articles_table)

sqliteConnection.close()