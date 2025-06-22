from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'choicehub53@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-password'  # Use environment variable in real case

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        msg = Message("New Contact Form Submission",
                      sender=email,
                      recipients=["choicehub53@gmail.com"])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)
        return redirect("/thank-you")
    return render_template("contact.html")

@app.route("/thank-you")
def thank_you():
    return render_template("thank-you.html")

if __name__ == "__main__":
    app.run(debug=True)
