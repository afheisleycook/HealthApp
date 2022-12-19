import sqlite3  
def setup():
    app = sqlite3.connect("app.db")
    with open("setupe.sql","r") as sql:
        for line in sql:
            app.execute(line)




setup()