from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail


app = Flask(__name__)
app.secret_key = 'complete'
csrf = CSRFProtect(app)

# Mail configuration
mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'sender email'
app.config["MAIL_PASSWORD"] = 'password'
mail.init_app(app)


from portfolio import routes