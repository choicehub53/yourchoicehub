from flask import Flask, render_template, request, redirect
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/appointment')
def appointment():
    return render_template('appointment.html')
    
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        print("CONTACT FORM RECEIVED")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)

        return "Contact form received successfully!"

    return render_template('contact.html')

@app.route('/card')
def card():
    return render_template('card.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')

def send_email(name, email, message):
    try:
        gmail_username = os.environ.get("GMAIL_USERNAME")
        gmail_app_password = os.environ.get("GMAIL_APP_PASSWORD")

        print("GMAIL USERNAME FOUND:", bool(gmail_username))
        print("GMAIL APP PASSWORD FOUND:", bool(gmail_app_password))

        content = f"""Subject: New Contact Form Submission

Name: {name}
Email: {email}

Message:
{message}
"""

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        print("Connecting to Gmail...")

        server.login(
            gmail_username,
            gmail_app_password
        )

        print("Gmail login successful")

        server.sendmail(
            gmail_username,
            gmail_username,
            content
        )

        print("EMAIL SENT SUCCESSFULLY")

        server.quit()

    except Exception as e:
        print("EMAIL ERROR:", repr(e))
        raise

if __name__ == '__main__':
    app.run(debug=True)
