from chatgpt import talkgpt
import pyinputplus as pypl
import sqlite3
from win10toast import ToastNotifier

notification = ToastNotifier()
conn = sqlite3.connect('chat_to_ai.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS chat
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer VARCHAR(50),
        ai VARCHAR(100))''')

while True:
    user = pypl.inputStr(prompt='Write Text... (max character number is 50) ')
    if len(user) > 50 : raise Exception("max character number is 50")
    print(talkgpt(user))
    cur.execute("INSERT INTO chat (customer,ai) VALUES (?, ?)", (user,talkgpt(user)))
    notification.show_toast( "SQLITE", "Data saved successfully",duration=5 )
    cont = pypl.inputYesNo(prompt='Have another question? ')
    if cont == 'no' : break



conn.commit()
cur.close()
conn.close()
