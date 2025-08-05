import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "darshanchouthai@gmail.com"
EMAIL_PASSWORD ="equa rbrb gzow owbw"  # Replace with your actual 16-character app password

def send_otp_email(to_email, otp):
    msg = EmailMessage()
    msg.set_content(f"Your OTP is: {otp}")
    msg['Subject'] = "Email Verification Code"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    try:
        smtplib.SMTP_SSL.debuglevel = 1  # Enable debug output
        # ✅ Explicitly set a valid hostname (important!)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, local_hostname="localhost") as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("✅ Email sent successfully.")
        return True
    except smtplib.SMTPAuthenticationError:
        print("❌ SMTP Auth failed. Check app password.")
    except smtplib.SMTPException as e:
        print(f"❌ SMTP error: {e}")
    except Exception as e:
        print(f"❌ General error: {e}")
    return False

# Run the test
if __name__ == "__main__":
    recipient_email = "chouthaidarshan@gmail.com"  # <- Change to test email
    otp_code = 123456
    send_otp_email(recipient_email, otp_code)
