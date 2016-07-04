
import time
import sys
import getpass
import mysql.connector
# import smtplib

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



# # Create a text/plain message
# msg = MIMEText("Hello, here is this week's access report.")

# # me == the sender's email address
# # you == the recipient's email address
# msg['Subject'] = 'Makerspace Weekly Access Report'
# msg['From'] = krisfargo@gmail.com
# msg['To'] = krisfargo@gmail.com

# # Send the message via our own SMTP server, but don't include the
# # envelope header.
# s = smtplib.SMTP('localhost')
# s.sendmail(me, [you], msg.as_string())
# s.quit()