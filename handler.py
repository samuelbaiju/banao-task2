import json
import os
import smtplib
from email.mime.text import MIMEText

def send_email(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        receiver_email = body.get("receiver_email")
        subject = body.get("subject")
        body_text = body.get("body_text")

        if not receiver_email or not subject or not body_text:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing required fields"})
            }

        sender_email = os.environ["SMTP_EMAIL"]
        sender_password = os.environ["SMTP_PASSWORD"]

        msg = MIMEText(body_text)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error", "details": str(e)})
        }
