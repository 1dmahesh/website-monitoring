import requests
import smtplib

URL = 'https://example.com/','https://examle1.com/'
EMAIL_ADD = "xxxxxxxx"
PASS = "xxxxxxx"

for list in URL:
 response1 = requests.get(URL[0])
 response2 = requests.get(URL[1])

def Responce_code():
   for res in response1: 
     if response1.status_code == 200:
        print(URL[0], 'is Running Fine, No need to worry')
        break
     else:
        print(URL[0], 'is down, Do Something!!!')
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADD, PASS)
            msg = "Subject: " + URL[0] + "  is down, Please check now"
            smtp.sendmail(EMAIL_ADD, EMAIL_ADD, msg)      
        break

def responce_code():
    for res in response2: 
     if response2.status_code == 200:
        print(URL[1],'is Running Fine, No need to worry')
        break
     else:
        print(URL[1], 'is down, Do Something!!!')

        with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADD, PASS)
            msg = "Subject: " + URL[1] + " is down, Please check Now"
            smtp.sendmail(EMAIL_ADD , EMAIL_ADD , msg)      
        break
         
Responce_code()

responce_code()
