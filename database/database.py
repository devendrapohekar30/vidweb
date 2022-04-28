import sqlite3

conn = sqlite3.connect('vidweb.db')
conn.execute("""
CREATE TABLE IF NOT EXISTS user(
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_name varchar(100) NOT NULL,
  contact varchar(100) NOT NULL,
  username varchar(100) NOT NULL,
  email varchar(100) NOT NULL UNIQUE,
  password varchar(100) NOT NULL
);
""")



conn.close()

def register_user(name,  contact, username, email, password):
    try:
        conn = sqlite3.connect('vidweb.db') 
        result = conn.execute("SELECT user_name FROM user").fetchall()
        id = len(result)+1
        name = "'"+name+"'"
        contact = "'"+contact+"'"
        username = "'"+username+"'"
        email = "'"+email+"'"
        password = "'"+password+"'"
        query = "INSERT INTO user VALUES ("+str(id)+", "+name+", "+contact+", "+username+", "+email+", "+password+ ");"
        conn.execute(query)
        conn.commit()
        conn.close()
        return("success")
    except Exception as e:
        print(e)
        return("error")

def login_user(email, password):
    try:
        conn = sqlite3.connect('vidweb.db') 
        email = "'"+email+"'"
        password = "'"+password+"'"
        query = "SELECT * FROM user WHERE email="+email+" AND password="+password+" ;"
        user = conn.execute(query).fetchone()
        conn.close()
        if user != []:
            return user
        return("error")
    except:
        return("error")
    
def get_user(username):
    try:
        username = "'"+username+"'"
        conn = sqlite3.connect('vidweb.db')
        query = "SELECT * FROM user WHERE username="+username+" ;"
        user = conn.execute(query).fetchone()
        conn.close()
        return user
    except:
        return None
    
def get_mp3songs():
    try:
        conn = sqlite3.connect('vidweb.db')
        query = "SELECT * FROM mp3songs WHERE category='mp3songs' ;"
        mp3songs = conn.execute(query).fetchall()
        conn.close()
        print(mp3songs)
        return mp3songs
    except Exception as e:
        print(e)
        return None
    
def get_gallary():
    try:
        conn = sqlite3.connect('vidweb.db')
        query = "SELECT * FROM gallary WHERE category='gallary' ;"
        gallary = conn.execute(query).fetchall()
        conn.close()
        return gallary
    except:
        return None
    
    
