# Copyright (c) 2025 Kemar Christie & Roberto James
# All rights reserved. Unauthorized use, copying, or distribution is prohibited.
# Contact kemar.christie@yahoo.com & robertojames91@gmail.com for licensing inquiries.
# Authors: Kemar Christie & Roberto James

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(receiver_email, cc_emails, gpa, threshold, programme, school, full_name,stdID):
    
    # Example usage
    sender_email = "academic.notifs@gmail.com"

    subject = "Academic Alert: Low GPA"
    body = (f"Dear {full_name} - #{stdID},\n"
            f"We are notifying you that your GPA has fallen to {gpa}, "
            f"which is at or below the acceptable threshold of {threshold}.\n\n"
            f"Program: {programme}\n"
            f"School: {school}\n\n"
            f"Best regards,\nYour University")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_password = "dooz bssh khdc ojnc"  # Use an app password if you have 2FA

    # Split CC emails if provided as a single string
    if isinstance(cc_emails, str):
        cc_emails = cc_emails.split(";")

    # Set up the email headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Cc'] = ", ".join(cc_emails)  # Add CC emails here
    message['Subject'] = subject

    # Attach the email body
    message.attach(MIMEText(body, 'plain'))
    
    try:
        # Set up the SMTP server connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        
        # Send the email to the main recipient and CC recipients
        all_recipients = [receiver_email] + cc_emails
        server.sendmail(sender_email, all_recipients, message.as_string())
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        server.quit()  # Close the connection
