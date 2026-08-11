from flask import Flask, render_template, request, redirect
import os
import resend

app = Flask(**name**)

# Resend API key

resend.api_key = os.environ.get("RESEND_API_KEY")

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

```
if request.method == 'POST':

    name = request.form.get('name', '')
    email = request.form.get('email', '')
    message = request.form.get('message', '')

    try:
        send_email(name, email, message)

        return redirect('/thank-you')

    except Exception as e:
        print("CONTACT EMAIL ERROR:", e)

        return """
        <h2>Unable to send your enquiry</h2>
        <p>Please try again later or contact us on WhatsApp.</p>
        <p>WhatsApp: 7977292916</p>
        """


return render_template('contact.html')
```

@app.route('/card')
def card():
return render_template('card.html')

@app.route('/thank-you')
def thank_you():
return render_template('thank-you.html')

def send_email(name, email, message):

```
params = {
    "from": "Your Choice Hub <onboarding@resend.dev>",

    "to": [
        "choicehub53@gmail.com"
    ],

    "subject": "New Enquiry - Your Choice Hub",

    "html": f"""
    <!DOCTYPE html>

    <html>
    <body style="font-family: Arial, sans-serif;">

        <h2 style="color:#0f3d36;">
            New Enquiry - Your Choice Hub
        </h2>

        <hr>

        <p>
            <strong>Name:</strong>
            {name}
        </p>

        <p>
            <strong>Email:</strong>
            {email}
        </p>

        <p>
            <strong>Message:</strong>
        </p>

        <div style="
            background:#f8f5ec;
            padding:20px;
            border-radius:10px;
            line-height:1.6;
        ">
            {message}
        </div>

        <br>

        <hr>

        <p style="color:#666;">
            This enquiry was submitted through the
            Your Choice Hub website.
        </p>

    </body>
    </html>
    """
}

response = resend.Emails.send(params)

print("EMAIL SENT:", response)
```

if **name** == '**main**':
app.run(
host='0.0.0.0',
port=int(os.environ.get('PORT', 5000))
)
