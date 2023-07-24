import smtplib

my_email = "alibr357@gmail.com"
password = "Parti456."

connection = smtplib.SMTP("smpt.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="alibr366@gmail.com", msg="Hello")
connection.close()