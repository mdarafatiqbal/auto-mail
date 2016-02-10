import smtplib
def mail_Connection(Sender, Password, Receiver):
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    #signature = "--Mail was automated through Python 3 program \n\n "
    conn.login(Sender, Password)
    conn.sendmail(Sender, Receiver, 'Subject:\n\nTest\nThis is an automated program built using Python 3\n\n ')
    conn.quit()

Sender = input("Enter the Sender Email-ID\n")
Password = input("Enter the Password\n")
Receiver = input("Enter the Receiver Email-ID\n")
mail_Connection(Sender, Password, Receiver)
