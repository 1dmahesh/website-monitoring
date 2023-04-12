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
  

# EXECUTING THE SCRIPT 

To run the script, First go inside the **scripts** folder & Use the below command..

`python .\website-monitoring.py`

# SCHEDULE
 For scheduling the script as per your requirements, You can use the scheduler library or crontab.
 
 scheduler library link --- **https://pypi.org/project/schedule/**.
