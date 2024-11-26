import time
import sqlite3 as sql 

def createDB():
    conn = sql.connect("autoconomiento.db")
    print ("base de dato de autoconocimiento creada")
    conn.commit()
    conn.close()
    
def createTable():
    conn = sql.connect("autoconocimiento.db")
    cursor =conn.cursor()
    cursor.execute
    ("""
    CREATE TABLE experiences (
    experience_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    description TEXT NOT NULL,
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
""")
    print("tabla creada")    
    conn.close()      
     
if __name__=="__main__":
   createDB()
   createTable()
         
        