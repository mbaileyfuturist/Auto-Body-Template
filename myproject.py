import os
from flask_sqlalchemy import SQLAlchemy
from forms import EstimateForm
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from models import IndexTable, CollisionRepair, Mechanical, Refining, db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

app.config.update(
    DEBUG=True,
    #EMAIL CONFIGURATION
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='',
    MAIL_PASSWORD=''
)
mail = Mail(app)

def send_email(name, email, phoneNumber, vehicleDetails, vehicleDescription):
    msg = Message('New Estimate Submission')
    sender = ''
    recipients = ['']
    msg.body= 'A new estimate form has been submitted: \n\n Name: ' + name + '\n\n Email: ' + email + '\n\n Phone Number: ' + phoneNumber + '\n\n Vehicle Details: ' + vehicleDetails + '\n\n Vehicle Description: ' + vehicleDescription
    mail.send(msg)


#Connect flask application to database.
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db.init_app(app)

#ROUTE SETUP.
@app.route('/', methods=['GET', 'POST'])
def root():
    form =  EstimateForm()
    if form.validate_on_submit():
        name = form.nameForm.data
        email = form.emailForm.data
        phoneNumber = form.numberForm.data
        vehicleDetails = form.vehicleDetailsForm.data
        vehicleDescription = form.vehicleDescriptionForm.data

        #Store data from form into SQLite database.
        new_submission = IndexTable(name, email, phoneNumber, vehicleDetails, vehicleDescription)
        db.session.add(new_submission)
        db.session.commit()

        #Send details of form submission via email.
        try:
            send_email(name, email, phoneNumber, vehicleDetails, vehicleDescription)
            return render_template('index.html', form=form)

        except Exception as e:
            return str(e)
    
    return render_template('index.html', form=form)



@app.route('/index.html', methods=['GET', 'POST'])
def index():
    form =  EstimateForm()
    
    if form.validate_on_submit():
        name = form.nameForm.data
        email = form.emailForm.data
        phoneNumber = form.numberForm.data
        vehicleDetails = form.vehicleDetailsForm.data
        vehicleDescription = form.vehicleDescriptionForm.data

        #Store data from form into SQLite database.
        new_submission = IndexTable(name, email, phoneNumber, vehicleDetails, vehicleDescription)
        db.session.add(new_submission)
        db.session.commit()

         #Send details of form submission via email.
        try:
            send_email(name, email, phoneNumber, vehicleDetails, vehicleDescription)
            return render_template('index', form=form)
        
        except Exception as e:
            return str(e)

    return render_template('index.html', form=form)



@app.route('/collision.html', methods=['GET', 'POST'])
def collision():
    form =  EstimateForm()
    
    if form.validate_on_submit():
        name = form.nameForm.data
        email = form.emailForm.data
        phoneNumber = form.numberForm.data
        vehicleDetails = form.vehicleDetailsForm.data
        vehicleDescription = form.vehicleDescriptionForm.data

        #Store data from form into SQLite database.
        new_submission = CollisionRepair(name, email, phoneNumber, vehicleDetails, vehicleDescription)
        db.session.add(new_submission)
        db.session.commit()

         #Send details of form submission via email.
        try:
            send_email(name, email, phoneNumber, vehicleDetails, vehicleDescription)
            return render_template('index', form=form)

        except Exception as e:
            return str(e)

    return render_template('collision.html', form=form)



@app.route('/mechanical.html', methods=['GET', 'POST'])
def mechanical():

    form =  EstimateForm()
    
    if form.validate_on_submit():
        name = form.nameForm.data
        email = form.emailForm.data
        phoneNumber = form.numberForm.data
        vehicleDetails = form.vehicleDetailsForm.data
        vehicleDescription = form.vehicleDescriptionForm.data

        #Store data from form into SQLite database.
        new_submission = Mechanical(name, email, phoneNumber, vehicleDetails, vehicleDescription)
        db.session.add(new_submission)
        db.session.commit()

         #Send details of form submission via email.
        try:
            send_email(name, email, phoneNumber, vehicleDetails, vehicleDescription)
            return render_template('index', form=form)

        except Exception as e:
            return str(e)
    
    return render_template('mechanical.html', form=form)



@app.route('/refining.html', methods=['GET', 'POST'])
def refining():

    form =  EstimateForm()
    
    if form.validate_on_submit():
        name = form.nameForm.data
        email = form.emailForm.data
        phoneNumber = form.numberForm.data
        vehicleDetails = form.vehicleDetailsForm.data
        vehicleDescription = form.vehicleDescriptionForm.data

        #Store data from form into SQLite database.
        new_submission = Refining(name, email, phoneNumber, vehicleDetails, vehicleDescription)
        db.session.add(new_submission)
        db.session.commit()

         #Send details of form submission via email.
        try:
            send_email(name, email, phoneNumber, vehicleDetails, vehicleDescription)
            return render_template('index', form=form)

        except Exception as e:
            return str(e)
    
    return render_template('refining.html', form=form)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')