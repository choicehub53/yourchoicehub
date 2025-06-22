import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'choicehub53@gmail.com'  # replace
app.config['MAIL_PASSWORD'] = 'choicehub*5253'        # replace

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send', methods=['POST'])
def send():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    msg = Message(subject=f"New Contact from {name}",
                  sender=email,
                  recipients=["choicehub53@gmail.com"],
                  body=message)
    mail.send(msg)
    return render_template('thank-you.html')

if __name__ == '__main__':
    app.run(debug=True)

