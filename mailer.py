import smtplib

message = "this email sent via python script"
#send via gmail server
server = smtplib.SMTP("smtp.gmail.com", 587) # https://support.google.com/a/answer/176600?hl=en
server.starttls() #start encryption
server.login("sender@email.com", "sender_password")
server.sendmail("senderr@email.com", "recipient@email.com", message)
# in order to send email without problems you must turn this on > https://myaccount.google.com/lesssecureapps
