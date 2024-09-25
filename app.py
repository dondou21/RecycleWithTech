from flask import Flask
from models import db
from routes import main_routes  

app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Register the routes
app.register_blueprint(main_routes)  # Registering the routes

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)