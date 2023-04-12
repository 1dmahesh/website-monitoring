
import requests
import smtplib

URL = ''
EMAIL = ""
PASS = ""

def check_urls():
    for url in URL:
        response = requests.get(url)
        if response.status_code == 200:
            print(url, 'is Running Fine, No need to worry')
        else:
            print(url, 'is down, Do Something!!!')
            try:
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.starttls()
                    smtp.ehlo()
                    smtp.login(EMAIL, PASS)
                    msg = "Subject: " + url + "  is down, Please check now"
                    smtp.sendmail(EMAIL, EMAIL, msg)
            except Exception as e:
                print("Error occurred while sending email notification:", e)

check_urls()
