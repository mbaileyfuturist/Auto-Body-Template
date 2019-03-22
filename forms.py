from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class EstimateForm(FlaskForm):
    nameForm = StringField('name')
    emailForm = StringField('email')
    numberForm = StringField('phone number')
    vehicleDetailsForm = StringField('make, model, year')
    vehicleDescriptionForm = StringField('vehicle description')
    submit = SubmitField('GET AN ESTIMATE')

