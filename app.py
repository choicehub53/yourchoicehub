from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/appointment")
def appointment():
    return render_template("appointment.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return redirect("/thank-you")

    return render_template("contact.html")


@app.route("/card")
def card():
    return render_template("card.html")


@app.route("/thank-you")
def thank_you():
    return render_template("thank-you.html")
