from flask import Flask, render_template, request, redirect
import smtplib
import os

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
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')

        send_email(name, email, message)

        return redirect('/thank-you')

    return render_template('contact.html')


@app.route('/card')
def card():
    return render_template('card.html')


@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')


def send_email(name, email, message):
    gmail_username = os.environ.get('GMAIL_USERNAME')
    gmail_app_password = os.environ.get('GMAIL_APP_PASSWORD')

    content = f"""Subject: New Contact Form Submission

Name: {name}
Email: {email}

Message:
{message}
"""

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(
        gmail_username,
        gmail_app_password
    )

    server.sendmail(
        gmail_username,
        gmail_username,
        content
    )

    server.quit()


if __name__ == '__main__':
    app.run(debug=True)
