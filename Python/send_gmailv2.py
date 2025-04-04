import json
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# File to log failed emails
list_of_email_not_sent = "listOfEmailNotSent.txt"

# Load JSON data
with open('spons_trial.json', 'r') as file:  # Always use trial JSON file when testing
    data = json.load(file)

email_user = 'gmail_id'  
email_password = 'app pass'  # Caution: Official Gmail password, use wisely
email_subject = 'Sponsorship Opportunity for Spectrum 2025'

# Gmail SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Image paths
banner_path = "spectrum.png"  # Replace with actual banner filename
logo_path = "gdg_vit.png"  # Replace with actual logo filename

# Check if images exist
if not os.path.exists(banner_path):
    print(f"Warning: Banner image '{banner_path}' not found.")
if not os.path.exists(logo_path):
    print(f"Warning: Logo image '{logo_path}' not found.")

for participant in data:
    name = participant['Name']
    email = participant['email_id']
    
    msg = MIMEMultipart("related")
    msg['From'] = email_user
    msg['To'] = email
    msg['Subject'] = email_subject

    # HTML Email body with inline images
    body = f"""
    <html>
        <body>
            <p><img src="cid:banner" width="600"></p>
            <p>Dear {name},</p>
            <p>I hope this message finds you well. I am writing on behalf of the <b>Google Developer Groups on Campus (GDG)</b> to invite your organization to sponsor <b>Spectrum 2025</b>, our flagship event focused on equipping students with valuable knowledge, hands-on experience, and certifications that will enhance their career prospects.</p>


            <p>At GDG, we bridge the gap between theoretical learning and real-world application. Our past events, including the Solution Challenge Offline Bootcamp, Gen AI Summit, and Google Developers Students Club (now GDG on Campus) Tech Fest, have made a significant impact on the tech community.</p>

            <p>For Spectrum 2025, we’re excited to expand beyond our campus, inviting participants from other colleges for a larger, dynamic event. We believe your sponsorship would be an excellent opportunity to showcase your brand to a highly engaged audience of students and professionals.</p>

            <p>Thank you for your time and consideration. I look forward to hearing from you.</p>

            <p>Best regards,<br>
            <b>Niranjan Jadhav</b><br>
            Finance and Sponsorship Lead,<br>
            Google Developer Groups on Campus, VIT<br>
            Contact: 8928995064</p>

            <p><img src="cid:logo" width="200"></p>
        </body>
    </html>
    """
    
    # Attach HTML content
    msg.attach(MIMEText(body, 'html'))

    # Attach banner image inline
    if os.path.exists(banner_path):
        with open(banner_path, "rb") as banner:
            img = MIMEImage(banner.read(), name=os.path.basename(banner_path))
            img.add_header('Content-ID', '<banner>')  # Inline reference
            img.add_header('Content-Disposition', 'inline')
            msg.attach(img)

    # Attach logo image inline
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as logo:
            img = MIMEImage(logo.read(), name=os.path.basename(logo_path))
            img.add_header('Content-ID', '<logo>')  # Inline reference
            img.add_header('Content-Disposition', 'inline')
            msg.attach(img)

    # Send email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.sendmail(email_user, email, msg.as_string())
        print(f"✅ Email sent to {name} at {email}")
    except Exception as e:
        print(f"❌ Failed to send email to {name} at {email}. Error: {e}")
        with open(list_of_email_not_sent, "a") as f:
            f.write(f"{name} \t {email} Failed \n")
