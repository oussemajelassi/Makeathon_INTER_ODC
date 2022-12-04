
import smtplib


smtpObj = smtplib.SMTP('smtp.gmail.com', 587) # or 465 ken 587 ma7abech
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('ahmedmarnissi1905@gmail.com', 'bvzozluxjonwsnwr') # mail li bch tab3ath bih

subject='ALERT: Anomaly detection'
body='ALERT: Anomaly detection'
msg=f'subject:{subject}\n\n{body}'

smtpObj.sendmail( 'ahmedmarnissi1905@gmail.com', 'gazze7achraf@gmail.com', msg)   
#                    li tab2ath bih               mail recepteur      #contenu



print ("Successfully sent email")