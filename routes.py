from flask import Blueprint, render_template, request, redirect, session
from models import db, User
from werkzeug.security import generate_password_hash

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid user')

    return render_template('login.html')

@main_routes.route('/contact')
def contact():
    return render_template('contact.html')

@main_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle request data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']  # Raw password
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        role = 'user'

        if not email or not password or not username:
            return render_template('signup.html', error='Please fill in all required fields.')

        # Create a new user instance with the raw password (hashing happens in the model)
        new_user = User(
            username=username,
            email=email,
            password=password,  # Pass raw password, it will be hashed in the model
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            role=role
        )

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')

    return render_template('signup.html')

@main_routes.route('/about')
def about():
    return render_template('about.html')

@main_routes.route('/items')
def items():
    return render_template('items.html')

@main_routes.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        username = request.form['username']
        return "Booking received"
    return render_template('booking.html')