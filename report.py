import mysql.connector
import csv
import sys
import getpass

passwordIn = getpass.getpass("Enter database password: ")

cnx = mysql.connector.connect(host='makerspace.unh.edu', user='rfid', password=passwordIn, database='database')
cursor = cnx.cursor()

cursor.execute("SELECT timestamp, user, affiliation FROM accessLog WHERE WEEKOFYEAR(timestamp)=WEEKOFYEAR(NOW())")

f = open(sys.argv[1], 'wt', newline='')
try:
	writer = csv.writer(f)
	writer.writerow( ('Timestamp', 'User', 'Affiliation') )
	print("Recording access from the following users: ")
	for (timestamp, user, affiliation) in cursor:
		print(timestamp, user, affiliation)
		writer.writerow((timestamp, user, affiliation))
finally:
    f.close()


cursor.close()
cnx.close()