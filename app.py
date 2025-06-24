from flask import Flask, render_template, request, redirect
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        send_email(name, email, message)
        return redirect('/thank-you')
    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')

def send_email(name, email, message):
    content = f"Subject:New Contact Form Submission\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("choicehub53@gmail.com", "pacggzipvlzuoxyo")  # change in deployment
    server.sendmail("choicehub53@gmail.com", "choicehub53@gmail.com", content)
    server.quit()

if __name__ == '__main__':
    app.run(debug=True)
