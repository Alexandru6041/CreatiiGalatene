import sqlite3
try:
    sqliteConnection = sqlite3.connect('main.db')
    cursor = sqliteConnection.cursor()
except sqlite3.Error as e:
    print("Error in database: " + e)
User_data_table = """
    CREATE TABLE UserData(
        Username VARCHAR(50) NOT NULL,
        Email VARCHAR(100) NOT NULL,
        User_Password VARCHAR(255) NOT NULL,
        Function VARCHAR(100) NOT NULL,
        Id INT
    );
"""
cursor.execute(User_data_table)
Articles_table = """
    CREATE TABLE Articles(
        Author VARCHAR(100) NOT NULL,
        Title VARCHAR(100) NOT NULL,
        Description VARCHAR(300) NOT NULL, 
        Context VARCHAR(1000000) NOT NULL,
        Function VARCHAR(100) NOT NULL,
        Email VARCHAR(100) NOT NULL,
        Id INT,
        Likes INT
    );
"""
cursor.execute(Articles_table)
Liked_table = """
    CREATE TABLE Liked(
        Id INT,
        Username VARCHAR(50) NOT NULL
    )
"""
cursor.execute(Liked_table)
sqliteConnection.close()