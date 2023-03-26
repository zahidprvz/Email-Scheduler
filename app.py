from flask import Flask, render_template, request
import smtplib
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule-email', methods=['POST'])
def schedule_email():
    recipient_email = request.form['recipient-email']
    email_subject = request.form['email-subject']
    number_of_days = int(request.form['number-of-days'])
    time_of_day = datetime.strptime(request.form['time-of-day'], '%H:%M').time()

    # Set up email message
    message = f"Subject: {email_subject}\n\n{request.form['message-body']}"

    # Set up email server
    email_server = smtplib.SMTP('smtp.gmail.com', 587)
    email_server.starttls()
    email_server.login('pervaizzahid55@gmail.com', 'qdnjjecciqgnscfa')

    # Schedule emails
    for i in range(number_of_days):
        send_time = datetime.now().replace(hour=time_of_day.hour, minute=time_of_day.minute, second=0, microsecond=0) + timedelta(days=i)
        email_server.sendmail('pervaizzahid55@gmail.com', recipient_email, message)
        print(f"Email scheduled for {send_time}")

    # Close email server
    email_server.quit()

    return 'Email scheduled successfully!'

if __name__ == '__main__':
    app.run(debug=True)

