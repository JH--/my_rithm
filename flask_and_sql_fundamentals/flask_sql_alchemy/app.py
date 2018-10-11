from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///computers_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Computer(db.Model):
    __tablename__ = "computers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    memory_in_gb = db.Column(db.Integer)

    def __init__(self, name, memory_in_gb):
        self.name = name
        self.memory_in_gb = memory_in_gb
    
    def __repr__(self):
        return f"This {self.name} has {self.memory_in_gb} GB of memory"