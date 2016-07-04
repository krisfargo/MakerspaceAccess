
import time
import sys
import mysql.connector

passwordIn = getpass.getpass("Enter database password: ")

cnx = mysql.connector.connect(host='makerspace.unh.edu', user='rfid', password=passwordIn, database='database')
cursor = cnx.cursor()

testVar = input("Enter tag ID: ")

cursor.execute("SELECT firstName,lastName,affiliation FROM members where members.rfidNumber like " + testVar)

for (firstName, lastName, affiliation) in cursor:
    name = "{} {}".format(firstName, lastName)
    affiliationid = affiliation

print(affiliationid)

add_entry = ("INSERT INTO accessLog (timestamp, user, affiliation) VALUES (%s, %s, %s)")
entry_data = (time.strftime("%Y-%m-%d %H:%M:%S"), name, affiliationid)

cursor.execute(add_entry, entry_data)

cursor.close()

cnx.commit()
cnx.close()