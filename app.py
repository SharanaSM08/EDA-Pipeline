from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

generated_email = ""
generated_otp = ""

# Home Page
@app.route('/', methods=['GET', 'POST'])
def home():

    global generated_email
    global generated_otp

    message = ""

    if request.method == 'POST':

        names = ["alex", "john", "cool", "user"]
        domains = ["gmail.com", "yahoo.com", "outlook.com"]

        generated_email = (
            random.choice(names)
            + str(random.randint(100,999))
            + "@"
            + random.choice(domains)
        )

        generated_otp = str(random.randint(100000,999999))

        message = "Email and OTP Generated"

    return render_template(
        'home.html',
        email=generated_email,
        otp=generated_otp,
        message=message
    )

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():

    global generated_email
    global generated_otp

    message = ""

    if request.method == 'POST':

        user_email = request.form['email']
        user_otp = request.form['otp']

        if (
            user_email == generated_email
            and user_otp == generated_otp
        ):

            with open("visitors.txt", "a") as file:
                file.write(user_email + "\n")

            return redirect('/success')

        else:
            message = "Wrong Email or OTP"

    return render_template(
        'login.html',
        message=message
    )

# Success Page
@app.route('/success')
def success():
    return render_template('success.html')

# Visitors Page
@app.route('/visitors')
def visitors():

    try:
        with open("visitors.txt", "r") as file:
            emails = file.readlines()
    except:
        emails = []

    total = len(emails)

    return render_template(
        'visitors.html',
        emails=emails,
        total=total
    )

if __name__ == '__main__':
    app.run(debug=True)