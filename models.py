import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#MODEL SETUP: The modal name by default will have the same name as your classname.
class IndexTable(db.Model):

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

class CollisionRepair(db.Model):
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

class Mechanical(db.Model):
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

class Refining(db.Model):
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