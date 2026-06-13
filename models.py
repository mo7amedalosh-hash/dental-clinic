from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(50), default='')
    address = db.Column(db.String(300), default='')
    age = db.Column(db.String(20), default='')
    treatment_type = db.Column(db.String(200), default='')
    treatment_history = db.Column(db.Text, default='')
    doctor_name = db.Column(db.String(100), default='')
    nurse_name = db.Column(db.String(100), default='')
    total_fees = db.Column(db.Float, default=0)
    amount_paid = db.Column(db.Float, default=0)
    remaining = db.Column(db.Float, default=0)
    notes = db.Column(db.Text, default='')
    created_at = db.Column(db.String(30), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    updated_at = db.Column(db.String(30), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    created_by = db.Column(db.String(20), default='reception')
    locked = db.Column(db.Integer, default=1)
    edit_requested = db.Column(db.Integer, default=0)

    edit_requests = db.relationship('EditRequest', backref='patient', lazy=True, cascade='all, delete-orphan')
    appointments = db.relationship('Appointment', backref='patient', lazy=True, cascade='all, delete-orphan')
    treatment_records = db.relationship('TreatmentRecord', backref='patient', lazy=True, cascade='all, delete-orphan')

class EditRequest(db.Model):
    __tablename__ = 'edit_requests'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    requested_at = db.Column(db.String(30), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    status = db.Column(db.String(20), default='pending')

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    appointment_date = db.Column(db.String(20), nullable=False)
    appointment_time = db.Column(db.String(10), default='')
    notes = db.Column(db.Text, default='')
    status = db.Column(db.String(20), default='scheduled')
    created_at = db.Column(db.String(30), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

class TreatmentRecord(db.Model):
    __tablename__ = 'treatment_records'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    record_date = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    doctor_name = db.Column(db.String(100), default='')
    nurse_name = db.Column(db.String(100), default='')
    cost = db.Column(db.Float, default=0)
    created_at = db.Column(db.String(30), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
