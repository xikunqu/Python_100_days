from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import  MIMEMultipart

import urllib

def main():

    #创建一个带附件的邮件消息对象
    message=MIMEMultipart()

    #创建文本内容
    text_content=MIMEText('用ython发送邮件的实力代码','olain','utf-8')
    message['Subject']=Header('亟待解决','utf-8')

    message.attach(text_content)


    with open('a.txt','rb') as f:
        txt=MIMEText(f.read(),'base64','utf-8')
        message.attach(txt)

    sender='568930245@qq.com'
    receivers=['quxikun7825@sina.com']

    smtper=SMTP('smtp.126.com')

    smtper.login(sender,'11234455')
    smtper.sendmail(sender,receivers,message.as_string())
    print('邮件发送完成')

if __name__=='__main__':
    main()
