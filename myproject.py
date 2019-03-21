import os
from forms import EstimateForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'
app.config.update(
    DEBUG=True,
)

#connect flask application to database.
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

db = SQLAlchemy(app)

#Modal setup: The modal name by default will have the same name as your classname.
class CollisionRepairTable(db.Model):

    #Create the columns.
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    phoneNumber = db.Column(db.Text)
    vehicleDetails = db.Column(db.Text)
    vehicleDescription = db.Column(db.Text)


    #id will be auto generated because its the primary key.
    def __init__(self, name, email, phoneNumber, vehicleDetails, vehicleDescription):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.vehicleDetails = vehicleDetails
        self.vehicleDescription = vehicleDescription

    #This method will give us a string repreentation of the columns
    def __repr__(self):
        return "Collision repair submission: Name: " + self.name + " Email: " + self.email + " Phone Number: " + self.phoneNumber + "Vehicle Details: " + self.vehicleDetails + "Vehicle Description: " + self.vehicleDescription
#################################################################################

#Route Setup.
@app.route('/', methods=['GET', 'POST'])
def root():
    form =  EstimateForm()

    if form.validate_on_submit():
        name = form.nameForm.data
        email = form.emailForm.data
        phoneNumber = form.numberForm.data
        vehicleDetails = form.vehicleDetailsForm.data
        vehicleDescription = form.vehicleDescriptionForm.data

        new_submission = CollisionRepairTable(name, email, phoneNumber, vehicleDetails, vehicleDescription)
        db.session.add(new_submission)
        db.session.commit()

        return render_template('index.html', form=form)
    
    return render_template('index.html', form=form)

@app.route('/index.html', methods=['GET', 'POST'])
def index():
    form =  EstimateForm()
    
    if form.validate_on_submit():
        db.create_all()
        name = form.nameForm.data
        email = form.emailForm.data
        phoneNumber = form.numberForm.data
        vehicleDetails = form.vehicleDetailsForm.data
        vehicleDescription = form.vehicleDescriptionForm.data

        new_submission = CollisionRepairTable(name, email, phoneNumber, vehicleDetails, vehicleDescription)
        db.session.add(new_submission)
        db.session.commit()
        return render_template('index', form=form)

    return render_template('index.html', form=form)

@app.route('/collision.html')
def collision():
    return render_template('collision.html')

@app.route('/mechanical.html')
def mechanical():
    return render_template('mechanical.html')

@app.route('/refining.html')
def refining():
    return render_template('refining.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0')

 