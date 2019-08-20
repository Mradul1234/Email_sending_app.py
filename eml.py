import smtplib 
import webbrowser

def get_email():
    serviceavail=['hotmail','gmail','outlook','yahoo']
    
   #mradulsingh0100@gmail.com
    while True:
        mail=input("enter sender mail id\n")
        if "@" in mail and ".com" in mail:
            rate=mail.find("@")
            com=mail.find(".com")
            sp=mail[rate+1:com]
            if sp in serviceavail:
                return (mail , sp)
                
                break
            else:
                print("entered service provider are not in our range select from gmail,yahoo,outlook,hotmail")
                continue
        else:
            print("wrong mail id you have entered")
            continue
email,service_provider = get_email()
print("your mail id is",email)
print("your service provider is ",service_provider)
def set_smtp_domain_name(service_provider):
    if service_provider=="gmail":
        return("smtp.gmail.com")
    elif service_provider=="yahoo":
        return("smtp.mail.yahoo.com")
    elif service_provider=="hotmail" or service_provider=="outlook":
        return("smtp-mail.outlook.com")
smtp_domain_name=set_smtp_domain_name(service_provider)
print("your smtp domain name is", smtp_domain_name)

def login():
    print("the sender mail id is",email)
    passwrd=input("enter your password")
    return(passwrd)
password=login()

def reciever_info():
    recieve=input("enter reciver emil id\n")
    sub=input("enter the subject\n")
    msg=input("enter the message here\n")
    return(recieve,sub,msg)
reciver_id,subject,message = reciever_info()
connection=smtplib.SMTP(smtp_domain_name,587)
connection.ehlo()
connection.starttls()
connection.login(email, password)
connection.sendmail(email , reciver_id ,("Subject : ", str(subject) , "\n\n " ,str(message)))
print("email send successfully")
connection.quit()
