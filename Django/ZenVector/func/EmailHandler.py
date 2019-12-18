import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Email_SendServer(message,toUser):

    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('puttogethersoftware@gmail.com', 'PutTogether123')

    mailserver.sendmail('puttogethersoftware@gmail.com',
                        toUser,
                        message)

def Email_SignUp(userEmail,name,accountType):
    msg = MIMEMultipart()
    msg['From'] = 'PutTogether Team'
    msg['To'] = userEmail
    msg['Subject'] = "Welcome to the PutTogether community!"
    if accountType == "F":
        features = "You are registered with the <b>Free</b> version, You will be able to create 5 projects only with 5 team members at max.\n" \
                   "You can upgrade your account any time to unleash your ability."
    elif accountType == 'P':
        features = "You are registered with the <b>Premium</b> version, You will be able to create 200 projects with 50 team members at max.\n" \
                   "You can upgrade your account any time to unleash your ability."
    else:
        features = "You are registered with the <b>Platinium</b> version, You will be able to create 1000 projects with 100 team members at max.\n" \
                   "Thank you for your trust."
    message = """
                <!DOCTYPE html>
                    <html>
                    <body style="padding-top: 20px; background-color: #f5f5f5;">

                    <div style="width:500px; margin: auto; background-color: white; border-radius: 5px; border-color: #59A61E; border-style: solid;">
                        <div style="text-align: center; color: white; background-color: #59A61E">
                        <img style="align-items: ;" src="https://res.cloudinary.com/di6zpszmk/image/upload/v1575834908/puttogether1-03_xzhhab.png" width="150" height="100">
                        </div>
                        <div style="padding: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif">
                        <strong style="color: black">Hello <b>{name}</b></strong>!
                        <p style="color: black;">Welcome to PutTogether! Are you ready to organize your life?</p>
                        <p>{features}</p>
                        <p>Thank you for creating a PutTogether account!</p>
                        <p>For any questions, You can reach us through <strong>PutTogetherSoftware@gmail.com</strong>.</p>
                        <p>-With love, PutTogether Team.</p>
                        </div>
                    </div>
                </body>
              """.format(name=name,features = features)
    msg.attach(MIMEText(message, 'html'))
    return msg.as_string()

def Email_PasswordResetCode(usrEmail,code):
    msg = MIMEMultipart()
    msg['From'] = 'PutTogether Team'
    msg['To'] = usrEmail
    msg['Subject'] = "Password Reset Code"
    message = """
                <!DOCTYPE html>
                    <html>
                    <body style="padding-top: 20px; background-color: #f5f5f5;">

                    <div style="width:500px; margin: auto; background-color: white; border-radius: 5px; border-color: #59A61E; border-style: solid;">
                        <div style="text-align: center; color: white; background-color: #59A61E">
                        <img style="align-items: ;" src="https://res.cloudinary.com/di6zpszmk/image/upload/v1575834908/puttogether1-03_xzhhab.png" width="150" height="100">
                        </div>
                        <div style="padding: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif">
                        <strong style="color: black">Whoops! You seem to have forgotten your password! </strong>
                        <p style="color: black;">You have requested to reset your account's password. </p>
                        <p>Please use the following code in the resetting process <b>{code}</b>.</p>
                        <p>For any questions, you can reach us through <strong>PutTogetherSoftware@gmail.com</strong>.</p>
                        <a href="http://127.0.0.1:8000/PutTogether/PasswordResetOut/{email}/{code}">click here</a>
                        <p>-With love, PutTogether Team.</p>
                        </div>
                    </div>
                </body>
              """.format(code=code,email=usrEmail)
    msg.attach(MIMEText(message, 'html'))

    return msg.as_string()

def Email_Contact_Us(usrEmail,subject,message):
    msg = MIMEMultipart()
    msg['From'] = 'puttogethersoftware@gmail.com'
    msg['To'] = 'PutTogether Team'
    msg['Subject'] = subject
    message = """
                <!DOCTYPE html>
                    <html>
                    <body style="padding-top: 20px; background-color: #f5f5f5;">

                    <div style="width:500px; margin: auto; background-color: white; border-radius: 5px; border-color: #59A61E; border-style: solid;">
                        <div style="text-align: center; color: white; background-color: #59A61E">
                        <img style="align-items: ;" src="https://res.cloudinary.com/di6zpszmk/image/upload/v1575834908/puttogether1-03_xzhhab.png" width="150" height="100">
                        </div>
                        <div style="padding: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif">
                        <p style="color: black;">Message from: {usrEmail}</p>
                        <p style="color: black;">Subject: {subject}</p>
                        <p></p>
                        <p style="color: black;">{message}</p>
                        </div>
                    </div>
                </body>
              """.format(usrEmail=usrEmail, subject=subject, message=message)
    msg.attach(MIMEText(message, 'html'))
    return msg.as_string()

def Email_Invitation_to_members(usrEmail,code):
    msg = MIMEMultipart()
    msg['From'] = 'PutTogether Team'
    msg['To'] = usrEmail
    msg['Subject'] = "Password Reset Code"
    message = """
                <!DOCTYPE html>
                    <html>
                    <body style="padding-top: 20px; background-color: #f5f5f5;">

                    <div style="width:500px; margin: auto; background-color: white; border-radius: 5px; border-color: #59A61E; border-style: solid;">
                        <div style="text-align: center; color: white; background-color: #59A61E">
                        <img style="align-items: ;" src="https://res.cloudinary.com/di6zpszmk/image/upload/v1575834908/puttogether1-03_xzhhab.png" width="150" height="100">
                        </div>
                        <div style="padding: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif">
                        <strong style="color: black"> Hey 'NAME of invited member', "Name of inviter" wants to collaborate with you!  </strong>
                        <p>Learn more here: </p>
                        <p>For any questions, you can reach us through <strong>PutTogetherSoftware@gmail.com</strong>.</p>
                        <a href="http://127.0.0.1:8000/PutTogether/PasswordResetOut/{email}/{code}">click here</a>
                        <p>-With love, PutTogether Team.</p>
                        </div>
                    </div>
                </body>
              """.format(code=code,email=usrEmail)
    msg.attach(MIMEText(message, 'html'))

    return msg.as_string()