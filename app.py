import os
from flask import Flask, render_template, request, redirect, url_for


from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the absolute path of the current directory
base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object('config.Config')
from flask import jsonify
from db import db
db.init_app(app)

from models import Employee

@app.route('/employees', methods=['GET'])
def list_employees():
    return jsonify([e.to_dict() for e in Employee.query.all()])


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)