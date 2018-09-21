import requests
from base64 import decodestring
import sqlite3
from subprocess import call
import os
os.chdir('C:\\Users\\Yashodeep Mahapatra\\Desktop\\For_Testing\\MSO Device Driver')
call(['setup'])
os.chdir('C:\\Users\\Yashodeep Mahapatra\\Desktop\\For_Testing')
conn = sqlite3.connect('fingerprints.db')
# conn.execute('''CREATE TABLE fingerprints(
# 	NAME TEXT NOT NULL,
# 	FINGERPRINT TEXT NOT NULL
# 	);''')
n = input("Enter number of persons whose fingerprints are to be entered")
for i in range(int(n)):
	name = input("Enter Name:")
	print("Place your finger on the machine...")
	response = requests.get("http://localhost:8080/CallMorphoAPI")
	img_data = response.json()['Base64BMPIMage']
	conn.execute("INSERT INTO fingerprints VALUES (?,?)",(name,img_data))
	conn.commit()
cursor = conn.execute("SELECT * FROM fingerprints")
for row in cursor:
	print('NAME: '+row[0],end = ' ')
	print('FINGERPRINT: '+str(row[1][:20]))
