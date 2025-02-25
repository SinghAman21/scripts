import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

listOfEmailNotSend = "listOfEmailNotSend.txt"

with open('', 'r') as file:
    data = json.load(file)

email_user = 'your@gmail'  
email_password = 'email code'  #email pass or app pass
email_subject = 'Thank You for attending the Figma Workshop'

# Gmail SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587

for participant in data:
    name = participant['Name']
    email = participant['email_id']
    certificate_filename = participant['Name']
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email
    msg['Subject'] = email_subject

    body = f"Dear {name},\n\nThank you for attending the Figma workshop hosted by GDG-VIT, Mumbai, in collaboration with Friends with Figma! Your participation made it a success.\n\nStay connected with us on https://linktr.ee/gdgvit for future updates and events!\n\nBest regards,\nMaitri Dalvi\nGDG-VIT, Mumbai"
    msg.attach(MIMEText(body, 'plain'))


    attachment_path = f"certificates/{certificate_filename}.png".strip()
    print(f"Checking file at path: {attachment_path}")

    if os.path.exists(attachment_path):
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename={certificate_filename}.png")
            msg.attach(part)

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email_user, email_password)
                text = msg.as_string()
                server.sendmail(email_user, email, text)
            print(f"Certificate sent to {name} at {email}")
        except Exception as e:
            print(f"Failed to send email to {name} at {email}. Error: {e}")
            with open(listOfEmailNotSend, "a") as f:
                f.write(f"{certificate_filename} \t {name} Failed \n")
    else:
        print(f"Certificate file {certificate_filename} not found. Skipping {name}.")
        with open(listOfEmailNotSend, "a") as f:
            f.write(f"{certificate_filename} \t {name} Not Found \n")
=======
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

listOfEmailNotSend = "listOfEmailNotSend.txt"

with open('', 'r') as file:
    data = json.load(file)

email_user = 'gdgoncampus.vit@gmail.com'  
email_password = 'wtmg vznd yzki hyeh'  #email pass or app pass
email_subject = 'Thank You for attending the Figma Workshop'

# Gmail SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587

for participant in data:
    name = participant['Name']
    email = participant['email_id']
    certificate_filename = participant['Name']
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email
    msg['Subject'] = email_subject

    body = f"Dear {name},\n\nThank you for attending the Figma workshop hosted by GDG-VIT, Mumbai, in collaboration with Friends with Figma! Your participation made it a success.\n\nStay connected with us on https://linktr.ee/gdgvit for future updates and events!\n\nBest regards,\nMaitri Dalvi\nGDG-VIT, Mumbai"
    msg.attach(MIMEText(body, 'plain'))


    attachment_path = f"certificates/{certificate_filename}.png".strip()
    print(f"Checking file at path: {attachment_path}")

    if os.path.exists(attachment_path):
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename={certificate_filename}.png")
            msg.attach(part)

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email_user, email_password)
                text = msg.as_string()
                server.sendmail(email_user, email, text)
            print(f"Certificate sent to {name} at {email}")
        except Exception as e:
            print(f"Failed to send email to {name} at {email}. Error: {e}")
            with open(listOfEmailNotSend, "a") as f:
                f.write(f"{certificate_filename} \t {name} Failed \n")
    else:
        print(f"Certificate file {certificate_filename} not found. Skipping {name}.")
        with open(listOfEmailNotSend, "a") as f:
            f.write(f"{certificate_filename} \t {name} Not Found \n")
