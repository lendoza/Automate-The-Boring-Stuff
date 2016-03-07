import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()

conn.starttls()

conn.login('labita.leonard@gmail.com', 'BLAHBLAH')

conn.sendmail('labita.leonard@gmail.com', 'labita.leonard@gmail.com')

conn.quit()