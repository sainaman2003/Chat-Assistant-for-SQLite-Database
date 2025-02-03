from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(),unique=True, nullable=False)
    department = db.Column(db.String(), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    hire_date = db.Column(db.Date, nullable=False)

class Departments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    manager = db.Column(db.String(), nullable=False)


