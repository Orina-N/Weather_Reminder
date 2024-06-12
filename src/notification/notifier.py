import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from conn2 import conn, cursor

# Function to send email notification
def send_email(recipient_email, subject, message):
    # Email configuration
    sender_email = "orinamecha@gmail.com"
    sender_password = "eyhp uiyv qfff twxk"
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

# Function to query rain percentage
def query_rain_percentage():
    sql = """
       SELECT rain_chance FROM weather_data WHERE date = 'Today' OR date = 'Tonight'
    """
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

# Function to check rain chance and send notification
def check_rain_and_notify(recipient_email):
    # Query rain chance
    rain_chance_result = query_rain_percentage()
    
    if rain_chance_result:
        rain_chance = int(rain_chance_result[0].strip('%'))
        
        # Define rain chance threshold (e.g., 50%)
        threshold = 5
        
        # Check if rain chance exceeds threshold
        if rain_chance >= threshold:
            # Send email notification
            subject = "Rain Alert!"
            message = "There is a high chance of rain today or tonight. Don't forget to take an umbrella!"
            send_email(recipient_email, subject, message)

# Example usage
recipient_email = "victor.wangari@student.moringaschool.com"
check_rain_and_notify(recipient_email)
