from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import bcrypt

db = SQLAlchemy()

# User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # Hashed password is stored here
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), unique=True)
    role = db.Column(db.String(20), nullable=False, default='user')  # Add this line with a default role
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    is_active = db.Column(db.Boolean, default=True)
    rewards_points = db.Column(db.Integer, default=0)

    # Property to set and hash password
    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute!")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def __init__(self, username, email, password, first_name, last_name, phone_number, role='user'):
        self.username = username
        self.email = email
        self.password = password  # This calls the setter and hashes the password
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.role = role

    def check_password(self,password):
            return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))
        
