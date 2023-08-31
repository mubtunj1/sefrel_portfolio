from flask import Flask, render_template, request, flash, redirect, url_for
from portfolio.form import ContactForm
from portfolio import app, mail, csrf
from flask_mail import Message



# Home route
@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = ContactForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            # try:
                msg = Message(form.subject.data, sender='developer@sefrel.com', recipients=['developer@sefrel.com'])
                msg.body = """ 
From: %s 
Email: <%s>
Subject: %s 
Message: %s 
                """ % (form.name.data, form.email.data, form.subject.data, form.message.data)
                # Create a separate connection context to send the email
                
                mail.send(msg)
                
                flash('Message sent', 'success')
                return redirect(url_for('home'))
            # except Exception as e:
            #     flash('An error occurred while sending the email. Please try again later.', 'danger')
            #     print(e)
    
    return render_template('index.html', form=form)


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio-details.html')



    


if __name__ == '__main__':
    app.run(debug=True)