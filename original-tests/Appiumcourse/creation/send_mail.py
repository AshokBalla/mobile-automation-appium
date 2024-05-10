import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "ashokooha143@gmail.com"
receiver_email = "ashok@gmail.com"

# For demonstration - use environment variables in production
# You can set these with: 
# export EMAIL_PASSWORD="your-app-password-here"
app_password = os.environ.get("EMAIL_PASSWORD", "")

try:
    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Test Email from Python"
    
    # Email body
    body = "Hello, this is a test email sent from Python!"
    message.attach(MIMEText(body, "plain"))
    
    # Connect to server
    print("Connecting to SMTP server...")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    if not app_password:
        print("WARNING: No EMAIL_PASSWORD environment variable found.")
        print("To set it: export EMAIL_PASSWORD='your-app-password'")
        print("\nINSTRUCTIONS TO CREATE APP PASSWORD:")
        print("1. Go to your Google Account settings")
        print("2. Select Security")
        print("3. Under 'Signing in to Google', select 'App passwords'")
        print("   (You may need to enable 2-Step Verification first)")
        print("4. Select 'Mail' and your device")
        print("5. Copy the generated password")
        print("6. Run: export EMAIL_PASSWORD='generated-password'")
        print("7. Then run this script again\n")
    else:
        # Login and send email
        print("Attempting login...")
        server.login(sender_email, app_password)
        
        print("Sending email...")
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully!")
    
    # Quit server
    server.quit()
    
except Exception as e:
    print(f"An error occurred: {e}")

# Run with: python3 send_mail.py