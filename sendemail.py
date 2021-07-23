import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("Arifkhanstar0786@gmail.com","Absrkhan078621")
message="hello I am Arif Khan"
connection.sendmail("Arifkhanstar0786@gmail.com","amarproject2021@gmail.com",message)
connection.quit()