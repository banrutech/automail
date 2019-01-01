#! /usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

def ReadFile(filename):
    with open(filename,'r') as f:
        lines = list(f)
        return lines

def ListToString(lists):
    string = ''.join(lists)
    return string 
    
def SendMail(addr,txt):
    to_addr = addr[0]
    from_addr = addr[1]
    mail_id = from_addr
    mail_pass = addr[2]

    subject = txt[0]
    body = ListToString(txt[1:]) 
    msg = MIMEText(body)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject 

    smtp = smtplib.SMTP_SSL('smtp.gmail.com')
    smtp.login(mail_id, mail_pass)
    smtp.sendmail(from_addr, to_addr, msg.as_string())
    smtp.quit

addr = ReadFile('pass.txt')
txt = ReadFile('mail.txt')

SendMail(addr, txt)
