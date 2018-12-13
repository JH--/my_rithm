from project import db

EmployeeDepartment = db.Table(
    "employee_departments",
    db.Column("id", db.Integer, primary_key=True),
    db.Column(
        "employee_id", db.Integer, db.ForeignKey("employees.id", ondelete="cascade")
    ),
    db.Column(
        "department_id", db.Integer, db.ForeignKey("departments.id", ondelete="cascade")
    ),
)


class Employee(db.Model):

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    years_at_company = db.Column(db.Integer)
    manager_id = db.Column(db.Integer, db.ForeignKey("employees.id"))
    departments = db.relationship(
        "Department", secondary=EmployeeDepartment, backref=db.backref("employees")
    )
    employees = db.relationship(
        "Employee", lazy="joined", backref=db.backref("manager", remote_side=[id])
    )
    # curious about the remote_side? See what happens if you try to remove it!

    def __init__(self, name, years_at_company, manager_id=None):
        self.name = name
        self.years_at_company = years_at_company
        self.manager_id = manager_id


class Department(db.Model):
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name
