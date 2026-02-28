from db import db


class Employee(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    designation = db.Column(db.String(128))
    years_of_experience = db.Column(db.Numeric)

    def to_dict(self):
        return {
            'employee_id':self.employee_id,
            'name':self.name,
            'designation':self.designation,
            'years_of_experience':self.years_of_experience
        }