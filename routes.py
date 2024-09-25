from flask import Blueprint, render_template, request

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@main_routes.route('/contact')
def contact():
    return render_template('contact.html')

@main_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        pass
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
        name = request.form['name']
        return "Booking received"
    return render_template('booking.html')