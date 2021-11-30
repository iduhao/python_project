#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from email import header
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.lantrack.net"  #设置服务器
mail_user="duhao@lantrack.net"    #用户名
mail_pass="Dh_38426"   #口令 
 
 
sender = 'duhao@lantrack.net'
receivers = ['duhao@lantrack.net']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('python邮件报警', 'plain', 'utf-8')
#message['From'] = sender
#message['From'] = Header('实时报警','utf-8')
h=Header('实时报警', 'utf-8')
h.append('<duhao@lantrack.net>', 'ascii')
message['From'] = h
#message["From"] = Header('实时报警', 'utf-8').append('<duhao@lantrack.net>', 'ascii')
message['To'] =  Header("测试", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as err:
    print ('error',err)