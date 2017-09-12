#Tool Name		: XSS_Detector
# Author		: Mayendran Govender
# Created               : 5 September 2014
# Version		: 1.0
# Description		: This tool scans through your webserver log to detect Cross site scripting attacks.The output is written to a file called XSS_Attacks.log
# Usage                 : python XSS_Detector.py

#Important Notice - Please test this Tool in a test platorm and understand how this tool works before using in a production platform. 

#Cross-site scripting (XSS)
# What is Cross Site script vulnerability - Often referred to a "XSS" is a code vulnerability in a website that allows an attacker to inject malicious client-side scripts into a web page. 


import platform		                # Loading the list of  Modules
import os
import subprocess
import sys
import datetime
import time


with open("XSS_Attacks.log","a+") as stdout: # The XSS_Attacks.log file is the output file that will contain Cross Site scripting payload attacks if there any detected.
   subprocess.Popen('cat xss.txt | grep "<script>alert"' ,  shell=True, stdout=stdout, stderr=stdout) # change xss.txt to your web server log file name (e.g. access_log or httpd.log)

import datetime 
f=open("XSS_Attacks.log",'a')
f.write ("Cross Site scripting attacks detected on"+'\t') # Adding a note to say XSS detected with today's date and time stamp into the output log
f.write ('\n')
f.write(datetime.datetime.now().ctime())

