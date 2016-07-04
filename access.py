
import time
import sys
import mysql.connector

cnx = mysql.connector.connect(host='makerspace.unh.edu', user='rfid', password='b72794b1282c70d3658edd5068373fc8', database='database')
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