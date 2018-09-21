from base64 import decodestring
import sqlite3
import os
conn = sqlite3.connect('fingerprints.db')
database = conn.execute("SELECT * FROM fingerprints")
string = {}
for row in database:
	string[row[0]] = (bytearray(row[1],'utf8'))
os.chdir('C:\\Users\\Yashodeep Mahapatra\\Desktop\\For_Testing\\python-fingerprint-recognition\\database')
for key in string:
	with open("%s.png"%(key),"wb") as f:
		f.write(decodestring(string[key]))