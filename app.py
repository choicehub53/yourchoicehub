from flask import Flask, render_template, request, redirect
import os
import resend

app = Flask(**name**)

resend.api_key = os.environ.get("RESEND_API_KEY")

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

```
    name = request.form.get("name", "")
    email = request.form.get("email", "")
    message = request.form.get("message", "")

    try:
        params = {
            "from": "Your Choice Hub <onboarding@resend.dev>",
            "to": ["choicehub53@gmail.com"],
            "subject": "New Enquiry - Your Choice Hub",
            "html": f"""
            <h2>New Enquiry - Your Choice Hub</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Message:</strong></p>
            <p>{message}</p>
            """
        }

        resend.Emails.send(params)

        return redirect("/thank-you")

    except Exception as e:
        print("CONTACT EMAIL ERROR:", e)
        return "Unable to send enquiry. Please try again later."

return render_template("contact.html")
```

@app.route("/card")
def card():
return render_template("card.html")

@app.route("/thank-you")
def thank_you():
return render_template("thank-you.html")

if **name** == "**main**":
app.run(
host="0.0.0.0",
port=int(os.environ.get("PORT", 5000))
)
)
