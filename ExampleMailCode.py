import smtplib
from email.mime.text import MIMEText
fp = open(textfile, 'rb')  ---- for reading File Data
msg = MIMEText("this the content")
msg['Subject'] = 'The contents of Test mail'
msg['From'] = 'tejas.suresh@emc.com'
msg['To'] = "tejas.suresh@emc.com"
s = smtplib.SMTP('localhost')
s.sendmail("tejas.suresh@XXX.com", ["tejas.suresh@XXX.com"], msg.as_string())
s.quit()
