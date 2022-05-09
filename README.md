# website-monitoring by python script

# CONTENTS
 1 - Images - Image of alert received in Gmail.
 
 2 - Scripts - Python Script to get the alerts.
 
 # REQUIREMENTS 
 This script is compatible only with `mac/windows-wsl/linux` OS
 
 Install python-3 in your system, below is the link to download if not downloaded 
 
 **https://www.python.org/downloads/**
 
 The script needs the below libraries of python.
 
 **requests**
 
 **smtplib**
 
 # CONFIGURATIONS
 Please add your email-id and password in **EMAIL_ADD** & **PASS** vairables.
 
 In **URL** , You can add multiple websites, that you want to monitor.
  
 If more than 2 websites are added in **URL**, then update **responce** variable according to the website count in **URL**.
 
 For more websites you can copy `responce_code()` function and update the values in it.

To receive alerts on email, go to the Images folder.

# EXECUTING THE SCRIPT 

To run the script, Use the below command..

`python .\website-monitoring.py`

# SCHEDULE
 For scheduling the script as per your requirements, You can use the scheduler library or crontab.
 
 scheduler library link --- **https://pypi.org/project/schedule/**.
